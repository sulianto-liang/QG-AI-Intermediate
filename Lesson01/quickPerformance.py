# Performance Example - Process a list of numbers
# Slow way (traditional loop)
slow_result = []
for num in [1, 2, 3, 4, 5]:
    slow_result.append(num * 2)

# Fast way (list comprehension)
fast_result = [num * 2 for num in [1, 2, 3, 4, 5]]

print("Slow result:", slow_result)
print("Fast result:", fast_result)
print("Same output:", slow_result == fast_result)