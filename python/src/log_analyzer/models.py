
from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class Incident:
    fingerprint: str
    severity: str
    count: int
    first_seen: str
    last_seen: str
    services: list[str]
    example_message: str
    recommendation: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
