class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# دریافت ورودی
name = input()
age = int(input())

# ایجاد شیء و نمایش
person = Person(name, age)
print(person)
