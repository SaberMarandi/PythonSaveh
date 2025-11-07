class Employee:
    def __init__(self, name, salary, bonus_rate):
        self.__name = name
        self.__salary = salary
        self.__bonus_rate = bonus_rate
    
    @property
    def name(self):
        return self.__name
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
    
    @property
    def bonus_rate(self):
        return self.__bonus_rate
    
    @bonus_rate.setter
    def bonus_rate(self, value):
        if 0 <= value <= 100:
            self.__bonus_rate = value
    
    @property
    def bonus(self):
        return self.__salary * self.__bonus_rate / 100
    
    @property
    def total_salary(self):
        return self.__salary + self.bonus

# دریافت ورودی
name = input()
salary = float(input())
bonus_rate = float(input())

employee = Employee(name, salary, bonus_rate)
print(f"کارمند: {employee.name}")
print(f"حقوق پایه: {employee.salary:.0f}")
print(f"پاداش: {employee.bonus:.0f}")
print(f"حقوق کل: {employee.total_salary:.0f}")
