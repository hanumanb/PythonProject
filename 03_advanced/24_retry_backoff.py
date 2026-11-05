"""Retry with exponential backoff and jitter; bounded attempts."""
import random
import time

def run_with_retry(operation, attempts=4, base_delay=0.2, max_delay=2.0):
    for attempt in range(attempts):
        try:
            return operation()
        except (TimeoutError, ConnectionError):
            if attempt == attempts - 1:
                raise
            delay = min(base_delay * (2 ** attempt), max_delay)
            delay += random.uniform(0, delay * 0.2)
            print(f"Retrying after {delay:.2f}s")
            time.sleep(delay)

if __name__ == "__main__":
    state = {"calls": 0}
    def flaky_operation():
        state["calls"] += 1
        if state["calls"] < 3:
            raise TimeoutError("temporary timeout")
        return "success"
    print(run_with_retry(flaky_operation))
