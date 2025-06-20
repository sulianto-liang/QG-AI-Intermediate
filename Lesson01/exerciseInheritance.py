# Your turn! Create a neural network hierarchy
import numpy as np

class BaseNeuralNetwork:
    def __init__(self, name, input_size, output_size):
        # TODO: Initialize common attributes
        self.name = name
        self.input_size = input_size
        self.output_size = output_size
        self.trained = False

    def initialize_weights(self):
        # TODO: Common weight initialization
        self.weights = np.random.randn(self.input_size, self.output_size)
        return self.weights

    def forward(self, inputs):
        # TODO: Base forward pass logic
        if not self.trained:
            print(f"{self.name} needs to be trained first!")
            return None
        print(f"Making forwarding with {self.name}...")
        return f"forwarding"

    def train(self, data, epochs):
        # TODO: Common training loop
        print(f"Training {self.name} with data {data}...")
        for epoch in range(epochs):
            print(f"Epoch {epoch + 1}/{epochs}")
        self.trained = True
        print(f"{self.name} data {data} has been trained!")


class ConvolutionalNN(BaseNeuralNetwork):
    def __init__(self, input_size, output_size, kernel_size=3):
        # TODO: Initialize with CNN-specific parameters
        super().__init__('CNN', input_size, output_size)
        super().train([1,2,3],kernel_size)
        print(f"Initializing Convolutional NN... with kernel_size={kernel_size}")

    def forward(self, inputs):
        # TODO: CNN-specific forward pass (convolution, pooling)
        super().forward(inputs)
        return f"{self.name} data {inputs} has been forwarded!"


class RecurrentNN(BaseNeuralNetwork):
    def __init__(self, input_size, output_size, hidden_size=128):
        # TODO: Initialize with RNN-specific parameters
        super().__init__('RNN',input_size, output_size)
        super().train([1,2,3],hidden_size)
        print(f"Initializing Recurrent NN... with hidden_size={hidden_size}")


    def forward(self, inputs):
        # TODO: RNN-specific forward pass (handle sequences)
        super().forward(inputs)
        return f"{self.name} data {inputs} has been forwarded!"


# Test your hierarchy
cnn = ConvolutionalNN(784, 10)
rnn = RecurrentNN(100, 5)
print("CNN forward:", cnn.forward([1, 2, 3]))
print("RNN forward:", rnn.forward([1, 2, 3]))
