
"""Deterministic log analyzer: parsing, grouping, severity and export."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Iterable

from .models import Incident

LOG_RE = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>TRACE|DEBUG|INFO|WARN|WARNING|ERROR|FATAL|CRITICAL|EXCEPTION)\s+"
    r"(?P<service>[\w.-]+)\s+(?P<message>.*)$",
    re.IGNORECASE,
)

SEVERITY = {
    "FATAL": "CRITICAL", "CRITICAL": "CRITICAL", "EXCEPTION": "HIGH",
    "ERROR": "HIGH", "WARN": "MEDIUM", "WARNING": "MEDIUM",
}

def normalize_message(message: str) -> str:
    """Normalize volatile numbers/IDs so repeated failures group together."""
    message = re.sub(r"\b\d+(?:\.\d+)?\b", "<N>", message.lower())
    message = re.sub(r"\s+", " ", message).strip()
    return message

def recommendation_for(message: str, severity: str) -> str:
    msg = message.lower()
    if "outofmemory" in msg or "heap space" in msg:
        return "Inspect heap usage and GC logs; capture a heap dump; check for leaks and right-size memory."
    if "timeout" in msg or "connection" in msg:
        return "Check dependency health, network path, connection-pool saturation, and timeout/retry settings."
    if "503" in msg or "unavailable" in msg:
        return "Verify dependency availability, service endpoints, capacity, and recent deployments."
    if "nullpointer" in msg:
        return "Inspect the referenced stack frame and validate inputs; add null-safe handling and regression tests."
    return f"Review correlated logs and recent changes; triage as {severity} before taking action."

def parse_line(line: str) -> dict | None:
    match = LOG_RE.match(line.strip())
    if not match:
        return None
    data = match.groupdict()
    data["level"] = data["level"].upper()
    if data["level"] not in SEVERITY:
        return None
    try:
        datetime.fromisoformat(data["timestamp"].replace(" ", "T"))
    except ValueError:
        return None
    return data

def analyze_lines(lines: Iterable[str]) -> list[Incident]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for line in lines:
        parsed = parse_line(line)
        if parsed:
            fingerprint = normalize_message(parsed["message"])
            groups[fingerprint].append(parsed)

    incidents: list[Incident] = []
    for fingerprint, events in groups.items():
        events.sort(key=lambda e: e["timestamp"])
        levels = [e["level"] for e in events]
        severity = max((SEVERITY[level] for level in levels),
                       key=lambda s: {"MEDIUM": 1, "HIGH": 2, "CRITICAL": 3}[s])
        services = sorted({e["service"] for e in events})
        example = events[0]["message"]
        incidents.append(Incident(
            fingerprint=fingerprint,
            severity=severity,
            count=len(events),
            first_seen=events[0]["timestamp"],
            last_seen=events[-1]["timestamp"],
            services=services,
            example_message=example,
            recommendation=recommendation_for(example, severity),
        ))
    return sorted(incidents, key=lambda i: (
        {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2}[i.severity], -i.count
    ))

def write_json(incidents: list[Incident], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps([i.to_dict() for i in incidents], indent=2), encoding="utf-8")

def write_csv(incidents: list[Incident], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = ["severity", "count", "services", "first_seen", "last_seen",
              "example_message", "recommendation", "fingerprint"]
    with output.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for incident in incidents:
            row = incident.to_dict()
            row["services"] = ", ".join(row["services"])
            writer.writerow({key: row[key] for key in fields})

def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze application logs and export incident report.")
    parser.add_argument("logfile", type=Path)
    parser.add_argument("--json", type=Path, default=Path("incident-report.json"))
    parser.add_argument("--csv", type=Path, default=Path("incident-report.csv"))
    args = parser.parse_args()

    if not args.logfile.exists():
        parser.error(f"Log file not found: {args.logfile}")
    incidents = analyze_lines(args.logfile.read_text(encoding="utf-8").splitlines())
    write_json(incidents, args.json)
    write_csv(incidents, args.csv)
    print(f"Analyzed {args.logfile}; found {len(incidents)} incident groups.")
    for item in incidents:
        print(f"[{item.severity}] {item.count}x {', '.join(item.services)}: {item.example_message}")
    print(f"JSON: {args.json}")
    print(f"CSV:  {args.csv} (Excel-friendly)")

if __name__ == "__main__":
    main()
