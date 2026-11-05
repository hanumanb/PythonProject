"""Iterator protocol."""
services = iter(["api", "worker", "database"])
while True:
    try:
        print(next(services))
    except StopIteration:
        break
