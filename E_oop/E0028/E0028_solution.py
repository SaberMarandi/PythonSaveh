import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# دریافت ورودی
a = float(input())
b = float(input())
c = float(input())

# ایجاد شیء و محاسبه
triangle = Triangle(a, b, c)
print(triangle.perimeter())
print(f"{triangle.area():.2f}")
