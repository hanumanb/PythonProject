"""Use context managers to manage resources safely."""
from pathlib import Path

path = Path("context_demo.txt")
with path.open("w", encoding="utf-8") as file:
    file.write("Context managers close files even if an error occurs.\n")

with path.open(encoding="utf-8") as file:
    print(file.read(), end="")
path.unlink(missing_ok=True)
