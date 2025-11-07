class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a // b
    
    def pow(self, a, b):
        return a ** b
    
    def mod(self, a, b):
        return a % b

# دریافت ورودی
num1 = int(input())
num2 = int(input())
operation = input()

# ایجاد شیء و انجام عملیات
calc = Calculator()

if operation == "add":
    result = calc.add(num1, num2)
elif operation == "sub":
    result = calc.sub(num1, num2)
elif operation == "mul":
    result = calc.mul(num1, num2)
elif operation == "div":
    result = calc.div(num1, num2)
elif operation == "pow":
    result = calc.pow(num1, num2)
elif operation == "mod":
    result = calc.mod(num1, num2)

print(result)
