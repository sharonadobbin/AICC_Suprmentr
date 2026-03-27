import time
import numpy as np

# Create data
size = 1_000_000

# Python list
py_list = list(range(size))

# NumPy array
np_array = np.arange(size)

# ---- Test 1: Addition ----
start = time.time()
py_result = [x + 5 for x in py_list]
end = time.time()
print("Python list addition time:", end - start)

start = time.time()
np_result = np_array + 5
end = time.time()
print("NumPy array addition time:", end - start)


# ---- Test 2: Multiplication ----
start = time.time()
py_result = [x * 2 for x in py_list]
end = time.time()
print("Python list multiplication time:", end - start)

start = time.time()
np_result = np_array * 2
end = time.time()
print("NumPy array multiplication time:", end - start)


# ---- Test 3: Squaring ----
start = time.time()
py_result = [x ** 2 for x in py_list]
end = time.time()
print("Python list squaring time:", end - start)

start = time.time()
np_result = np_array ** 2
end = time.time()
print("NumPy array squaring time:", end - start)