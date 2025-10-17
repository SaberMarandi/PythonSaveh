# E0001 - کلاس ساده
# ایجاد کلاس Person

class Person:
    def __init__(self, name):
        self.name = name

name = input()
p = Person(name)
print(p.name)
