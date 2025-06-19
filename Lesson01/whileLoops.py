# While Loops for AI Applications
print("=== Training Simulation with While Loop ===")
accuracy = 0.5
epoch = 0
target_accuracy = 0.9

while accuracy < target_accuracy and epoch < 10:
    epoch += 1
    # Simulate improving accuracy
    accuracy += 0.05 + (epoch * 0.01)
    print(f"Epoch {epoch}: Accuracy = {accuracy:.3f}")

if accuracy >= target_accuracy:
    print(f"Target accuracy reached in {epoch} epochs!")
else:
    print("Training stopped due to max epochs reached")

print("\n=== Data Processing with While Loop ===")
data_queue = ['sample1', 'sample2', 'sample3', 'sample4']
processed = 0

while data_queue:
    current_sample = data_queue.pop(0)
    processed += 1
    print(f"Processing {current_sample} (Total processed: {processed})")

print("All data processed!")