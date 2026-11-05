"""ThreadPoolExecutor for concurrent I/O-style tasks."""
from concurrent.futures import ThreadPoolExecutor
import time

def check_endpoint(name):
    time.sleep(0.1)  # simulate I/O
    return f"{name}: 200 OK"

if __name__ == "__main__":
    endpoints = ["health", "ready", "metrics"]
    with ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(check_endpoint, endpoints):
            print(result)
