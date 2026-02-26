# E0004 - کلاس مستطیل
# محاسبه مساحت و محیط مستطیل

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

w = int(input())
h = int(input())
rect = Rectangle(w, h)
print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")
