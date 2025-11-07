import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

# دریافت ورودی
x = float(input())
y = float(input())

# ایجاد شیء و محاسبه
point = Point(x, y)
print(f"{point.distance_from_origin():.2f}")
