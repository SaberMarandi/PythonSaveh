class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age

# دریافت ورودی
name = input()
age = int(input())

person = Person(name, age)
print(f"نام: {person.get_name()}, سن: {person.get_age()}")

# تغییر مقادیر
new_name = input()
new_age = int(input())

person.set_name(new_name)
person.set_age(new_age)
print(f"نام: {person.get_name()}, سن: {person.get_age()}")
