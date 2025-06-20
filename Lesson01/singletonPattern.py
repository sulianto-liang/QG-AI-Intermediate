# Singleton Pattern Example
class DataProcessor:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.processed_count = 0
            self._initialized = True
            print("DataProcessor initialized")

    def process_data(self, data):
        self.processed_count += 1
        print(f"Processing data batch #{self.processed_count}: {data}")
        return f"processed_{data}"


# Test Singleton
processor1 = DataProcessor()
processor2 = DataProcessor()

print(f"Are they the same instance? {processor1 is processor2}")

processor1.process_data("batch_1")
processor2.process_data("batch_2")

print(f"Total processed by processor1: {processor1.processed_count}")
print(f"Total processed by processor2: {processor2.processed_count}")