# Simple OOP Example - A Basic Robot
class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 100

    def say_hello(self):
        return f"Hello! I'm {self.name} and my battery is at {self.battery}%"


# Create a robot and make it talk
my_robot = Robot("AI-Bot")
print(my_robot.say_hello())