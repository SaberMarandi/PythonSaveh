class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# دریافت ورودی
animal_type = input()
name = input()

if animal_type == "dog":
    animal = Dog(name)
elif animal_type == "cat":
    animal = Cat(name)

print(f"{animal.name}: {animal.speak()}")
