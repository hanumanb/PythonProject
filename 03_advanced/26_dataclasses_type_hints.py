"""Dataclasses and type hints make data models clear."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Alert:
    service: str
    severity: str
    message: str

def is_actionable(alert: Alert) -> bool:
    return alert.severity.upper() in {"HIGH", "CRITICAL"}

if __name__ == "__main__":
    alert = Alert("payments", "CRITICAL", "Database unavailable")
    print(alert)
    print("Actionable:", is_actionable(alert))
