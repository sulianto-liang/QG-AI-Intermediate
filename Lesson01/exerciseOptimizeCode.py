# Your turn! Optimize this inefficient code
import time

def bad_data_processing(data):
    start_time = time.time()
    # This code works but is slow and hard to read
    result = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data[i])):
            if data[i][j] > 0:
                temp.append(data[i][j] * 2)
        if len(temp) > 0:
            result.append(temp)
    end_time = time.time()
    return result, start_time, end_time

# Test data
test_data = [
    [1, -2, 3, 0, 5],
    [-1, 0, 2, 4],
    [0, -3, -1],
    [2, 4, 6, 8]
]

# Your optimized version here:
def optimized_data_processing(data):
    # TODO: Rewrite using list comprehensions, better variable names, type hints, docstring
    start_time2 = time.time()
    result2 = [
        [
            data[i][j] * 2 for j in range(len(data[i]))
            if data[i][j] > 0
        ]
        for i in range(len(data))
        if len([
            data[i][j] * 2 for j in range(len(data[i]))
            if data[i][j] > 0
        ]) > 0
    ]
    end_time2 = time.time()
    return result2, start_time2, end_time2

# Test both versions
#print("Original result:", bad_data_processing(test_data))
#print("Optimized result:", optimized_data_processing(test_data))
original_result, ori_start_time, ori_end_time = bad_data_processing(test_data)
optimized_result, opt_start_time, opt_end_time = optimized_data_processing(test_data)

print(f"Original loop time: start: {ori_start_time:.6f}, stop: {ori_end_time:.6f}")
print(f"Optimized loop time: start: {opt_start_time:.6f}, stop: {opt_end_time:.6f}")
#print(f"Optimized loop is {original_time/optimized_time:.2f}x faster")
print(f"Both methods produce same result: {original_result == optimized_result}")
print("Original result:", original_result)
print("Optimized result:", optimized_result)
