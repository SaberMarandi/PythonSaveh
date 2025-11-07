class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade
    
    @property
    def name(self):
        return self.__name
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        if 0 <= value <= 20:
            self.__grade = value
        else:
            print("نمره باید بین 0 تا 20 باشد")
    
    @property
    def status(self):
        if self.__grade >= 10:
            return "قبول"
        else:
            return "مردود"

# دریافت ورودی
name = input()
grade = float(input())

student = Student(name, grade)
print(f"نام: {student.name}")
print(f"نمره: {student.grade}")
print(f"وضعیت: {student.status}")

new_grade = float(input())
student.grade = new_grade
print(f"نمره: {student.grade}")
print(f"وضعیت: {student.status}")
