# E0051 - وراثت ساده
# کلاس Animal و Dog

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

name = input()
dog = Dog(name)
print(dog.speak())
