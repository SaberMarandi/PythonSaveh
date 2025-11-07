# E0004 - متدهای کلاس
# کلاس مستطیل با متدهای محاسبه مساحت و محیط

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

length = int(input())
width = int(input())

rect = Rectangle(length, width)
print(rect.area())
print(rect.perimeter())
