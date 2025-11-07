class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

# دریافت ورودی
shape_type = input()
color = input()

if shape_type == "rectangle":
    length = float(input())
    width = float(input())
    shape = Rectangle(color, length, width)
elif shape_type == "circle":
    radius = float(input())
    shape = Circle(color, radius)

print(f"رنگ: {shape.color}")
print(f"مساحت: {shape.area():.2f}")
