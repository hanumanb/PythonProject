"""Write a CSV report that opens cleanly in Excel."""
import csv
from pathlib import Path

rows = [
    {"service": "payments", "severity": "HIGH", "count": 3},
    {"service": "inventory", "severity": "MEDIUM", "count": 1},
]
output = Path("incident-summary.csv")
with output.open("w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=["service", "severity", "count"])
    writer.writeheader()
    writer.writerows(rows)
print(f"Created {output.resolve()}")
