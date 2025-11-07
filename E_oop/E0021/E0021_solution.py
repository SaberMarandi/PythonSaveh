class School:
    school_name = ""
    
    def __init__(self, student_name):
        self.student_name = student_name
    
    def display(self):
        return f"دانشجو: {self.student_name}"

# دریافت ورودی
School.school_name = input()
n = int(input())

students = []
for i in range(n):
    name = input()
    students.append(School(name))

print(f"مدرسه: {School.school_name}")
for student in students:
    print(student.display())
