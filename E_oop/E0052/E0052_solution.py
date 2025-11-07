class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def display(self):
        return f"{super().display()} - {self.doors} درب"

# دریافت ورودی
brand = input()
model = input()
doors = int(input())

car = Car(brand, model, doors)
print(car.display())
