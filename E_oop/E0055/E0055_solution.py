class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        return f"نام: {self.name}, سن: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade
    
    def display(self):
        return f"{super().display()}, شماره دانشجویی: {self.student_id}, نمره: {self.grade}"

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    
    def display(self):
        return f"{super().display()}, درس: {self.subject}, حقوق: {self.salary}"

# دریافت ورودی
person_type = input()
name = input()
age = int(input())

if person_type == "student":
    student_id = int(input())
    grade = float(input())
    person = Student(name, age, student_id, grade)
elif person_type == "teacher":
    subject = input()
    salary = float(input())
    person = Teacher(name, age, subject, salary)

print(person.display())
