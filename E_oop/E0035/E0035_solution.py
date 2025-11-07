class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
    
    def __str__(self):
        return f"دانشجو: {self.name} ({self.student_id}) - نمره: {self.grade}"
    
    def __repr__(self):
        return f"Student('{self.name}', {self.student_id}, {self.grade})"

# دریافت ورودی
name = input()
student_id = int(input())
grade = float(input())

# ایجاد شیء و نمایش
student = Student(name, student_id, grade)
print(str(student))
print(repr(student))
