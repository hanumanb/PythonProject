"""Process a large text file line-by-line instead of loading it all into RAM."""
from pathlib import Path

source = Path("../sample_data/application.log")
error_count = 0
with source.open(encoding="utf-8") as file:
    for line in file:
        if " ERROR " in line or " FATAL " in line or " EXCEPTION " in line:
            error_count += 1
print("Error-like lines:", error_count)
