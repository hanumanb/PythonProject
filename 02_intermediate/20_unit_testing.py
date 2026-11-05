"""A small function designed to be tested with pytest."""
def retry_delay(attempt: int, base_seconds: float = 1.0, cap_seconds: float = 30.0) -> float:
    if attempt < 0:
        raise ValueError("attempt cannot be negative")
    return min(base_seconds * (2 ** attempt), cap_seconds)

if __name__ == "__main__":
    for attempt in range(6):
        print(attempt, retry_delay(attempt))
