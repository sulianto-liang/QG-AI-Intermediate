# List Comprehensions vs Regular Loops
import time

# Method 1: Regular loop
def regular_loop_method():
    start_time = time.time()
    result = []
    for i in range(10000):
        if i % 2 == 0:
            result.append(i * 2)
    end_time = time.time()
    return result, end_time - start_time

# Method 2: List comprehension
def list_comprehension_method():
    start_time = time.time()
    result = [i * 2 for i in range(10000) if i % 2 == 0]
    end_time = time.time()
    return result, end_time - start_time

# Test both methods
regular_result, regular_time = regular_loop_method()
comprehension_result, comprehension_time = list_comprehension_method()

print(f"Regular loop time: {regular_time:.6f} seconds")
print(f"List comprehension time: {comprehension_time:.6f} seconds")
print(f"List comprehension is {regular_time/comprehension_time:.2f}x faster")
print(f"Both methods produce same result: {regular_result == comprehension_result}")