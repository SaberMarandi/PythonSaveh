# E0005 - کلاس دایره
# محاسبه مساحت و محیط دایره

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius

r = float(input())
circle = Circle(r)
print(f"Area: {circle.area():.2f}, Circumference: {circle.circumference():.2f}")
