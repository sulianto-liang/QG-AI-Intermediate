# Basic Class Example
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{self.name} is a {self.breed}"


# Create an instance
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())
print(my_dog.get_info())