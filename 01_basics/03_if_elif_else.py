"""Conditional logic: classify an alert."""
def classify_cpu(cpu: float) -> str:
    if not 0 <= cpu <= 100:
        raise ValueError("CPU must be between 0 and 100")
    if cpu >= 95:
        return "CRITICAL"
    elif cpu >= 85:
        return "WARNING"
    return "NORMAL"

for value in (42, 88, 97):
    print(value, classify_cpu(value))
