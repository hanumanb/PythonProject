"""Practical file-based log analyzer: count levels and top services."""
from collections import Counter
from pathlib import Path

path = Path("../sample_data/application.log")
levels = Counter()
services = Counter()

with path.open(encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(maxsplit=3)
        if len(parts) < 4:
            continue
        level = parts[2].upper()
        service_and_message = parts[3].split(maxsplit=1)
        if level in {"INFO", "WARN", "WARNING", "ERROR", "FATAL", "EXCEPTION"}:
            levels[level] += 1
        if service_and_message:
            services[service_and_message[0]] += 1

print("Levels:", dict(levels))
print("Top services:", services.most_common(5))
