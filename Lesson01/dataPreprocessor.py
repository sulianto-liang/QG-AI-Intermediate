# Your turn! Create a DataPreprocessor class
# Hint: Use __init__ to initialize attributes
# Hint: Use methods to organize functionality
# Hint: Track method calls with counters

class DataPreprocessor:
    def __init__(self, dataset_name, dataset_size):
        # TODO: Initialize your attributes here
        self._dataset_name = dataset_name
        self._dataset_size = dataset_size
        self._normalize_method_called = 0
        self._split_method_called = 0
        self._get_info_method_called = 0

    def normalize_data(self):
        # TODO: Implement data normalization
        print(f"{self._dataset_name} is normalizing...")
        self._normalize_method_called += 1

    def split_data(self, train_ratio=0.8):
        # TODO: Implement data splitting
        print(f"{self._dataset_name} is splitting...")
        self._split_method_called += 1

    def get_info(self):
        # TODO: Return information about the preprocessor
        self._get_info_method_called += 1
        return {
            'dataset_name': self._dataset_name,
            'dataset_size': self._dataset_size,
            'normalize_method_called': self._normalize_method_called,
            'split_method_called': self._split_method_called,
            'get_info_method_called': self._get_info_method_called,
        }

# Test your class
preprocessor = DataPreprocessor("MNIST", 60000)
print(preprocessor.get_info())
preprocessor.normalize_data()
preprocessor.split_data()
print(preprocessor.get_info())