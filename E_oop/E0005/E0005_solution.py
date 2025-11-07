class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display(self):
        return f"نام: {self.name}, سن: {self.age}, نمره: {self.grade}"

# دریافت ورودی
name = input()
age = int(input())
grade = float(input())

# ایجاد شیء و نمایش اطلاعات
student = Student(name, age, grade)
print(student.display())
