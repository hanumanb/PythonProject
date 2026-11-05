"""List, dict, and set comprehensions."""
latencies_ms = [30, 120, 250, 45, 500]
slow_requests = [value for value in latencies_ms if value >= 100]
labels = {value: ("slow" if value >= 100 else "normal") for value in latencies_ms}
print("Slow:", slow_requests)
print("Labels:", labels)
