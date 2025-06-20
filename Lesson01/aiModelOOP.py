# AI Model Class Example
class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights_initialized = False
        self.training_history = []

    def initialize_weights(self):
        # Simulate weight initialization
        self.weights_initialized = True
        print(f"Initialized weights for {self.input_size} -> {self.hidden_size} -> {self.output_size} network")

    def forward(self, inputs):
        if not self.weights_initialized:
            self.initialize_weights()

        # Simulate forward pass
        print(f"Processing {len(inputs)} inputs through network")
        return [0.5, 0.3, 0.2]  # Mock output

    def train(self, data, epochs):
        print(f"Training network for {epochs} epochs on {len(data)} samples")
        for epoch in range(epochs):
            loss = 1.0 - (epoch * 0.1)  # Simulated decreasing loss
            self.training_history.append(loss)
            print(f"Epoch {epoch + 1}: Loss = {loss:.2f}")

    def get_model_info(self):
        return {
            "architecture": f"{self.input_size}-{self.hidden_size}-{self.output_size}",
            "weights_initialized": self.weights_initialized,
            "training_epochs": len(self.training_history)
        }


# Example usage
model = SimpleNeuralNetwork(784, 128, 10)  # MNIST-like network
fake_data = [[1, 2, 3, 4]] * 5  # Mock training data

print("Model Info:", model.get_model_info())
output = model.forward([1, 2, 3, 4])
print("Model Output:", output)

model.train(fake_data, 3)
print("After Training:", model.get_model_info())