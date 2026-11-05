"""Regular expressions: parse a structured log line."""
import re

line = "2026-11-05 09:03:42 ERROR payments Database timeout"
pattern = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<level>INFO|WARN|ERROR|FATAL) (?P<service>\w+) (?P<message>.*)$"
)
match = pattern.match(line)
if match:
    print(match.groupdict())
else:
    print("Unrecognized log format")
