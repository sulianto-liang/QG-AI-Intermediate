# Simple Inheritance Example
class Vehicle:  # Parent class
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} vehicle is starting..."


class Car(Vehicle):  # Child class inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent's __init__
        self.model = model

    def honk(self):
        return f"{self.brand} {self.model} goes BEEP BEEP!"


# Create a car and use both parent and child methods
my_car = Car("Toyota", "Camry")
print(my_car.start())  # From parent class
print(my_car.honk())  # From child class