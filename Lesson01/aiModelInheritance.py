# AI Model Inheritance Example
class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.trained = False
        self.training_history = []

    def preprocess_data(self, data):
        print(f"Preprocessing data for {self.model_name}")
        return data  # Mock preprocessing

    def train(self, data, epochs):
        processed_data = self.preprocess_data(data)
        print(f"Training {self.model_name} for {epochs} epochs")

        # Simulate training with improving accuracy
        for epoch in range(epochs):
            accuracy = min(50 + epoch * 10, 95)  # Increasing accuracy
            self.training_history.append(accuracy)
            print(f"Epoch {epoch + 1}: Accuracy = {accuracy}%")

        self.trained = True
        print(f"{self.model_name} training complete!")

    def predict(self, input_data):
        if not self.trained:
            print(f"{self.model_name} needs to be trained first!")
            return None
        print(f"Making prediction with {self.model_name}")
        return "prediction"

    def get_model_info(self):
        return {
            "name": self.model_name,
            "trained": self.trained,
            "epochs_completed": len(self.training_history)
        }


class LinearRegressionModel(BaseModel):
    def __init__(self):
        super().__init__("Linear Regression")
        self.coefficients = None

    def fit(self, X, y):  # Specialized training method
        print("Fitting linear regression model using least squares")
        self.coefficients = [0.5, 1.2]  # Mock coefficients
        self.trained = True
        print("Linear regression fitted successfully!")

    def predict(self, X):
        if not self.trained:
            print("Linear regression model needs to be trained first!")
            return None
        print("Making linear regression predictions")
        return [1.5, 2.3, 3.1]  # Mock predictions


class DecisionTreeModel(BaseModel):
    def __init__(self, max_depth=5):
        super().__init__("Decision Tree")
        self.max_depth = max_depth
        self.tree_structure = None

    def train(self, data, epochs):
        # Override parent train method with tree-specific logic
        processed_data = self.preprocess_data(data)
        print(f"Building decision tree with max depth: {self.max_depth}")

        # Simulate tree building
        self.tree_structure = f"Tree with {self.max_depth} levels"
        print(f"Decision tree structure: {self.tree_structure}")

        self.trained = True
        self.training_history = [85]  # Trees don't train in epochs
        print("Decision tree training complete!")

    def predict(self, input_data):
        if not self.trained:
            print("Decision tree needs to be trained first!")
            return None
        print("Making decision tree predictions")
        return ["class_A", "class_B", "class_A"]


# Test the model hierarchy
print("=== Linear Regression ===")
lr_model = LinearRegressionModel()
print(lr_model.get_model_info())
lr_model.fit([[1, 2], [3, 4]], [1, 2])
print("LR Results:", lr_model.predict([[7, 8]]))

print("\n=== Decision Tree ===")
dt_model = DecisionTreeModel(max_depth=10)
print(dt_model.get_model_info())
dt_model.train([[1, 2], [3, 4]], 1)  # Trees don't need epochs
print("DT Results:", dt_model.predict([[7, 8]]))