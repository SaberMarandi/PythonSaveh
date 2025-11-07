class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# دریافت ورودی
n = int(input())
animals = []

for i in range(n):
    animal_type = input()
    name = input()
    
    if animal_type == "dog":
        animals.append(Dog(name))
    elif animal_type == "cat":
        animals.append(Cat(name))
    elif animal_type == "cow":
        animals.append(Cow(name))

for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")
