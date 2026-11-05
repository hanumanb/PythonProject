"""Read CSV data with the standard csv module."""
import csv
from pathlib import Path

path = Path("../sample_data/services.csv")
with path.open(newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["service"], row["owner"], row["criticality"])
