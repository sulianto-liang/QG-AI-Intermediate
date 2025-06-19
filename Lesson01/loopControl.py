# Loop Control for Smart Processing
print("=== Early Stopping with Break ===")
training_losses = [1.0, 0.8, 0.6, 0.4, 0.45, 0.47, 0.48]  # Loss starts increasing

for epoch, loss in enumerate(training_losses, 1):
    print(f"Epoch {epoch}: Loss = {loss}")

    if epoch > 1 and loss > training_losses[epoch - 2]:
        print("Loss is increasing - stopping training early!")
        break

print("\n=== Skipping Bad Data with Continue ===")
data_samples = [100, -50, 200, 0, 150, -30, 300]

print("Processing valid samples (positive numbers only):")
processed_count = 0
for sample in data_samples:
    if sample < 0:
        print(f"Skipping invalid sample: {sample}")
        continue

    # Process valid sample
    processed_count += 1
    result = sample * 2
    print(f"Sample {sample} -> Processed: {result}")

print(f"Total valid samples processed: {processed_count}")