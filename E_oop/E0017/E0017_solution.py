class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def is_square(self):
        return self.length == self.width

# دریافت ورودی
length = float(input())
width = float(input())

# ایجاد شیء و بررسی
rect = Rectangle(length, width)

if rect.is_square():
    print("مربع")
else:
    print("مستطیل")
