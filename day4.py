import numpy as np
import time

# 1. Dot product - recreate Day 1's hand-calculated example
print("--- 1. Dot product ---")
a = np.array([4, 1])
b = np.array([2, 4])
print(f"a · b (np.dot) = {np.dot(a, b)}")
print(f"a · b (@)      = {a @ b}")  # same thing, different syntax

# 2. Matrix-vector multiplication - extend Day 2's 2x2 example to 3x3
print("\n--- 2. Matrix-vector multiplication (3x3) ---")
M = np.array([
    [2, 1, 0],
    [0, 3, 1],
    [1, 0, 2],
])
v = np.array([4, 1, 2])
print(f"M @ v = {M @ v}")

# 3. Eigenvalues/eigenvectors - compare against Day 3's intuition
print("\n--- 3. Eigenvalues & eigenvectors ---")
M2 = np.array([
    [2, 1],
    [0, 1],
])
eigenvalues, eigenvectors = np.linalg.eig(M2)
print(f"eigenvalues:  {eigenvalues}")
print(f"eigenvectors (as columns):\n{eigenvectors}")
# sanity check: M2 @ eigenvector should equal eigenvalue * eigenvector
for i in range(len(eigenvalues)):
    lhs = M2 @ eigenvectors[:, i]
    rhs = eigenvalues[i] * eigenvectors[:, i]
    print(f"  check {i}: M @ v = {lhs}, λ * v = {rhs}  (should match)")

# 4. Bonus - loop vs vectorized dot product benchmark
print("\n--- 4. Loop vs np.dot benchmark ---")
N = 1_000_000
x = np.random.rand(N)
y = np.random.rand(N)

start = time.perf_counter()
loop_result = sum(x[i] * y[i] for i in range(N))
loop_time = time.perf_counter() - start
print(f"pure Python loop: {loop_time:.4f}s")

start = time.perf_counter()
np_result = np.dot(x, y)
np_time = time.perf_counter() - start
print(f"np.dot:           {np_time:.4f}s")
print(f"speedup: {loop_time / np_time:.0f}x")