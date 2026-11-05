"""Find files by extension using pathlib."""
from pathlib import Path

for path in Path("../sample_data").glob("*.log"):
    print(path.name, path.stat().st_size, "bytes")
