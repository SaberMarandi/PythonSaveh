class Employee:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Employee.count += 1

# دریافت ورودی
n = int(input())

employees = []
for i in range(n):
    name = input()
    employees.append(Employee(name))

print(f"تعداد کارمندان: {Employee.count}")
for emp in employees:
    print(emp.name)
