import time
import functools


def timer(func):
    """Prints how long the wrapped function took to run."""
    @functools.wraps(func)  # preserves func's name/docstring — always do this
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timer] {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


@timer
def slow_add(a, b):
    time.sleep(0.3)
    return a + b


def retry(n=3):
    """Decorator FACTORY: retry() runs first and returns the actual decorator."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"[retry] {func.__name__} failed on attempt {attempt}: {e}")
            raise last_exception
        return wrapper
    return decorator


_call_count = 0

@retry(n=3)
def flaky():
    global _call_count
    _call_count += 1
    if _call_count < 3:
        raise ValueError(f"not ready yet (call {_call_count})")
    return "success!"


def batch(iterable, size):
    """Yields successive chunks of `iterable`, each up to `size` long."""
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:  # leftover partial chunk
        yield chunk


if __name__ == "__main__":
    print(slow_add(2, 3))
    print(flaky())

    data = list(range(1, 11))  # 1..10
    for group in batch(data, 3):
        print("[batch]", group)

    # Bonus: same idea as a generator expression (works for sliceable data)
    batches_expr = (data[i:i + 3] for i in range(0, len(data), 3))
    for group in batches_expr:
        print("[batch expr]", group)