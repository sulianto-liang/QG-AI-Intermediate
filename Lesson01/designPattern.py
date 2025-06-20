# Quick Pattern Example - Factory Pattern
class ModelFactory:
    @staticmethod
    def create_model(model_type):
        if model_type == "simple":
            return "Simple AI Model Created!"
        elif model_type == "advanced":
            return "Advanced AI Model Created!"
        else:
            return "Unknown model type"

# Create different models easily
print(ModelFactory.create_model("simple"))
print(ModelFactory.create_model("advanced"))
print(ModelFactory.create_model("whatever"))