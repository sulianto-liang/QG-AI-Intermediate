# Generators vs Lists for Memory Efficiency
import sys

# Regular list approach
def create_large_list(n):
    return [x**2 for x in range(n)]

# Generator approach
def create_large_generator(n):
    return (x**2 for x in range(n))

# Compare memory usage
n = 10000

# List approach
large_list = create_large_list(n)
list_size = sys.getsizeof(large_list)

# Generator approach
large_generator = create_large_generator(n)
generator_size = sys.getsizeof(large_generator)

print(f"List size: {list_size} bytes")
print(f"Generator size: {generator_size} bytes")
print(f"Memory saved: {list_size - generator_size} bytes")
print(f"Generator uses {generator_size/list_size*100:.2f}% of list memory")

# Demonstrate generator usage
print("\nFirst 10 squares from generator:")
for i, square in enumerate(large_generator):
    if i >= 10:
        break
    print(f"{i}² = {square}")