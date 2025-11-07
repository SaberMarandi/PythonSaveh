import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius

# دریافت ورودی
radius = float(input())

# ایجاد شیء و محاسبه
circle = Circle(radius)
print(f"{circle.area():.2f}")
print(f"{circle.circumference():.2f}")
