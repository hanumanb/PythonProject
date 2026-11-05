"""A timing decorator; useful for measuring function execution."""
from functools import wraps
from time import perf_counter

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"{func.__name__} took {perf_counter() - start:.6f}s")
    return wrapper

@measure_time
def sum_numbers(limit):
    return sum(range(limit))

print(sum_numbers(1_000_000))
