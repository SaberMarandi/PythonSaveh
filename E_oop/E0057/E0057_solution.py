class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    
    def get_salary(self):
        return self.salary + self.bonus

class Developer(Employee):
    def __init__(self, name, salary, projects):
        super().__init__(name, salary)
        self.projects = projects
    
    def get_salary(self):
        return self.salary + (self.projects * 1000000)

# دریافت ورودی
employee_type = input()
name = input()
salary = float(input())

if employee_type == "manager":
    bonus = float(input())
    employee = Manager(name, salary, bonus)
elif employee_type == "developer":
    projects = int(input())
    employee = Developer(name, salary, projects)

print(f"کارمند: {employee.name}")
print(f"حقوق: {employee.get_salary():.0f}")
