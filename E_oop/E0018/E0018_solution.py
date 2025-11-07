class StudentList:
    def __init__(self):
        self.students = []
    
    def add_student(self, name):
        self.students.append(name)
    
    def get_count(self):
        return len(self.students)
    
    def display(self):
        print(f"تعداد: {self.get_count()}")
        for student in self.students:
            print(student)

# دریافت ورودی
n = int(input())
student_list = StudentList()

for i in range(n):
    name = input()
    student_list.add_student(name)

student_list.display()
