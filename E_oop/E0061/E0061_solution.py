class Shape:
    def calculate_area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

# دریافت ورودی
shape_type = input()

if shape_type == "square":
    side = float(input())
    shape = Square(side)
elif shape_type == "triangle":
    base = float(input())
    height = float(input())
    shape = Triangle(base, height)

print(f"مساحت: {shape.calculate_area():.2f}")
