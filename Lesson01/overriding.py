# Method Overriding vs Extension Example
class BaseProcessor:
    def __init__(self, name):
        self.name = name
        self.processed_count = 0

    def process(self, data):
        print(f"Base processing with {self.name}")
        self.processed_count += 1
        return f"processed_{data}"


class ImageProcessor(BaseProcessor):
    def __init__(self):
        super().__init__("Image Processor")

    # Method OVERRIDING - completely replace parent behavior
    def process(self, data):
        print(f"Specialized image processing: resize, normalize, augment")
        self.processed_count += 1
        return f"image_processed_{data}"


class TextProcessor(BaseProcessor):
    def __init__(self):
        super().__init__("Text Processor")

    # Method EXTENSION - add to parent behavior
    def process(self, data):
        print("Text-specific preprocessing: tokenization, cleaning")
        # Call parent method to keep shared functionality
        result = super().process(data)
        print("Text-specific postprocessing: stemming, lemmatization")
        return f"text_{result}"


# Test both approaches
print("=== Image Processor (Override) ===")
img_proc = ImageProcessor()
result1 = img_proc.process("photo.jpg")
print(f"Result: {result1}")
print(f"Count: {img_proc.processed_count}")

print("\n=== Text Processor (Extension) ===")
text_proc = TextProcessor()
result2 = text_proc.process("hello world")
print(f"Result: {result2}")
print(f"Count: {text_proc.processed_count}")