"""Read and write text files safely with pathlib."""
from pathlib import Path

source = Path("../sample_data/notes.txt")
destination = Path("notes-output.txt")

text = source.read_text(encoding="utf-8")
destination.write_text(text.upper(), encoding="utf-8")
print(destination.read_text(encoding="utf-8"))
destination.unlink(missing_ok=True)
