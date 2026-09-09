import asyncio
import time


async def fetch_data(name, delay):
    """Simulates an I/O-bound call (like a network request)."""
    print(f"[start] {name} (will take {delay}s)")
    await asyncio.sleep(delay)  # non-blocking "wait" — other tasks can run meanwhile
    print(f"[done]  {name}")
    return f"{name}'s result"


async def sequential_demo():
    print("--- sequential (await one at a time) ---")
    start = time.perf_counter()
    r1 = await fetch_data("task_a", 1)
    r2 = await fetch_data("task_b", 1)
    r3 = await fetch_data("task_c", 1)
    print(f"sequential total: {time.perf_counter() - start:.2f}s\n")


async def concurrent_demo():
    print("--- concurrent (asyncio.gather) ---")
    start = time.perf_counter()
    r1, r2, r3 = await asyncio.gather(
        fetch_data("task_a", 1),
        fetch_data("task_b", 1),
        fetch_data("task_c", 1),
    )
    print(f"concurrent total: {time.perf_counter() - start:.2f}s")


async def main():
    await sequential_demo()
    await concurrent_demo()


async def flaky_fetch(name, fail_times=2):
    """Simulates an API call that fails a couple times before succeeding."""
    attempt = 0
    while True:
        attempt += 1
        await asyncio.sleep(0.3)
        if attempt <= fail_times:
            print(f"[retry] {name} failed on attempt {attempt}")
            continue
        print(f"[success] {name} succeeded on attempt {attempt}")
        return f"{name}-data"


async def async_retry_demo():
    print("--- async retry, run concurrently for two 'endpoints' ---")
    results = await asyncio.gather(
        flaky_fetch("endpoint_1", fail_times=2),
        flaky_fetch("endpoint_2", fail_times=1),
    )
    print("results:", results)


if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(async_retry_demo())