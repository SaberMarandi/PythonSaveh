class Car:
    def __init__(self, name, color="White"):
        self.name = name
        self.color = color
    
    def display(self):
        return f"نام: {self.name}, رنگ: {self.color}"

# دریافت ورودی
name = input()
has_color = input()

if has_color == "yes":
    color = input()
    car = Car(name, color)
else:
    car = Car(name)

print(car.display())
