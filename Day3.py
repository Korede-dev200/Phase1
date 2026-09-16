import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def cpu_bound_work(n):
    """Pure computation - sum of squares up to n. No I/O, no waiting."""
    return sum(i * i for i in range(n))



N = 20_000_000
CALLS = 4


def run_sequential():
    print("---sequential---")
    start = time.perf_counter()
    results = [cpu_bound_work(N) for _ in range(CALLS)]
    print(f"sequential: {time.perf_counter() - start:.2f}s for {CALLS} calls")
    return results


def run_threaded():
    print("--- threaded (ThreadPoolExecutor) ---")
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=CALLS) as pool:
        result = list(pool.map(cpu_bound_work, [N] * CALLS))
    print(f"threaded: {time.perf_counter() - start:.2f}s for {CALLS} calls")
    return result


def run_multiprocess():
    print("--- multiprocess (ProcessPoolExecutor) ---")
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=CALLS) as pool:
        result = list(pool.map(cpu_bound_work, [N] * CALLS))
    print(f"multiprocess: {time.perf_counter() - start:.2f}s for {CALLS} calls")
    return result


if __name__ == "__main__":
    run_sequential()
    run_threaded()
    run_multiprocess()