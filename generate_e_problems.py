"""
اسکریپت تولید خودکار مسائل پوشه E_oop
"""

import os

# تعریف مسائل باقیمانده
problems = {
    # Polymorphism (E0061-E0070)
    "E0061": {
        "title": "چندریختی ساده",
        "level": "متوسط",
        "description": "برنامه‌ای بنویسید که چندریختی را با متد calculate_area برای اشکال مختلف نشان دهد.",
        "input": "نوع شکل و ابعاد",
        "output": "مساحت",
        "solution": """class Shape:
    def calculate_area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

shape_type = input()
if shape_type == "square":
    side = float(input())
    shape = Square(side)
elif shape_type == "triangle":
    base = float(input())
    height = float(input())
    shape = Triangle(base, height)

print(f"مساحت: {shape.calculate_area():.2f}")"""
    },
    
    "E0062": {
        "title": "پلی‌مورفیسم با حیوانات",
        "level": "متوسط",
        "description": "برنامه‌ای بنویسید که لیستی از حیوانات مختلف ایجاد کند و متد make_sound را فراخوانی کند.",
        "input": "تعداد حیوانات و اطلاعات آن‌ها",
        "output": "صدای هر حیوان",
        "solution": """class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

n = int(input())
animals = []

for i in range(n):
    animal_type = input()
    name = input()
    
    if animal_type == "dog":
        animals.append(Dog(name))
    elif animal_type == "cat":
        animals.append(Cat(name))
    elif animal_type == "cow":
        animals.append(Cow(name))

for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")"""
    },
}

# تولید فایل‌های باقیمانده
for code, data in problems.items():
    folder = f"E_oop/{code}"
    
    # ایجاد فایل سوال
    question_file = f"{folder}/{code}_question.md"
    question_content = f"""# سوال {code} - {data['title']}

## سطح: {data['level']}

## صورت مسئله
{data['description']}

## ورودی
{data['input']}

## خروجی
{data['output']}

## راهنمایی
- از وراثت و بازنویسی متد استفاده کنید
"""
    
    with open(question_file, 'w', encoding='utf-8') as f:
        f.write(question_content)
    
    # ایجاد فایل راه‌حل
    solution_file = f"{folder}/{code}_solution.py"
    with open(solution_file, 'w', encoding='utf-8') as f:
        f.write(data['solution'])
    
    print(f"✅ {code} ایجاد شد")

print("\n✨ تولید مسائل کامل شد!")
