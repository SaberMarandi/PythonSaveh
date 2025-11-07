class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

# دریافت ورودی
x = int(input())
y = int(input())

# ایجاد شیء و نمایش
point = Point(x, y)
print(point)
