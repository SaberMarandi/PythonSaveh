class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value):
        if value > 0:
            self.__length = value
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
    
    @property
    def area(self):
        return self.__length * self.__width

# دریافت ورودی
length = float(input())
width = float(input())

rect = Rectangle(length, width)
print(f"مساحت: {rect.area}")

new_length = float(input())
new_width = float(input())

rect.length = new_length
rect.width = new_width
print(f"مساحت: {rect.area}")
