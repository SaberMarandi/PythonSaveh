class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
    
    @property
    def diameter(self):
        return self.__radius * 2
    
    @property
    def area(self):
        import math
        return math.pi * self.__radius ** 2
    
    @property
    def circumference(self):
        import math
        return 2 * math.pi * self.__radius

# دریافت ورودی
radius = float(input())
circle = Circle(radius)

print(f"شعاع: {circle.radius}")
print(f"قطر: {circle.diameter}")
print(f"مساحت: {circle.area:.2f}")
print(f"محیط: {circle.circumference:.2f}")
