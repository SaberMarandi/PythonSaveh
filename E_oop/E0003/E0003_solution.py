# E0003 - چند attribute
# کلاس Student

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

name = input()
age = int(input())
student = Student(name, age)
print(student.display())
