# Basic Inheritance Example
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def get_info(self):
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} fetches the ball!"


# Test inheritance
dog = Dog("Buddy", "Labrador")
print(dog.get_info())
print(dog.make_sound())
print(dog.fetch())