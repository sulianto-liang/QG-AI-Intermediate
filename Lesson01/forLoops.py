# Basic For Loops
print("=== Basic For Loop ===")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")

print("\n=== For Loop with Range ===")
for i in range(5):
    print(f"Index: {i}, Value: {i * 2}")

print("\n=== For Loop with Enumerate ===")
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("\n=== For Loop with Zip ===")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")