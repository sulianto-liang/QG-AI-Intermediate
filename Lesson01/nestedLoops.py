# Nested Loops for AI Data Processing
print("=== Processing 2D Data (like images) ===")
# Simulate a small 3x3 image
image_data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Original image:")
for row in image_data:
    print(row)

print("\nApplying brightness filter (+10):")
brightened_image = []
for row in image_data:
    new_row = []
    for pixel in row:
        new_pixel = pixel + 10
        new_row.append(new_pixel)
    brightened_image.append(new_row)

for row in brightened_image:
    print(row)

print("\n=== Training on Multiple Datasets ===")
datasets = ['dataset1', 'dataset2', 'dataset3']
models = ['model_a', 'model_b']

for dataset in datasets:
    for model in models:
        print(f"Training {model} on {dataset}")
        # Simulate training time
        print(f"  -> Training completed!")