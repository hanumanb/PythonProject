"""Read JSON, update a value, and write JSON."""
import json
from pathlib import Path

source = Path("../sample_data/config.json")
config = json.loads(source.read_text(encoding="utf-8"))
config["environment"] = "interview-lab"
Path("config-output.json").write_text(
    json.dumps(config, indent=2), encoding="utf-8"
)
print(config)
