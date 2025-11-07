class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    def display(self):
        print(f"نام: {self.name}")
        print(f"میانگین: {self.average():.2f}")

# دریافت ورودی
name = input()
n = int(input())
grades = list(map(float, input().split()))

# ایجاد شیء و نمایش
student = Student(name, grades)
student.display()
