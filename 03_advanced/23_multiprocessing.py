"""ProcessPoolExecutor for CPU-bound work (small illustrative workload)."""
from concurrent.futures import ProcessPoolExecutor

def sum_squares(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    inputs = [100_000, 150_000, 200_000]
    with ProcessPoolExecutor() as pool:
        print(list(pool.map(sum_squares, inputs)))
