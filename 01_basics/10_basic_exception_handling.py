"""try/except/else/finally."""
raw_value = "not-a-number"
try:
    replicas = int(raw_value)
except ValueError as exc:
    print(f"Invalid replica count: {exc}")
else:
    print("Replicas:", replicas)
finally:
    print("Validation finished")
