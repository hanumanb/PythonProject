"""String parsing and cleanup."""
raw = "  ERROR: payment-service connection timeout  "
clean = raw.strip()
level, message = clean.split(":", maxsplit=1)
print(level.upper())
print(message.strip().replace("-", " ").title())
