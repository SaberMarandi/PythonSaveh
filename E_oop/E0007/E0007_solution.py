class MathOperations:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a // b

# دریافت ورودی
num1 = int(input())
num2 = int(input())
operation = input()

# ایجاد شیء و انجام عملیات
math_ops = MathOperations()

if operation == "add":
    result = math_ops.add(num1, num2)
elif operation == "subtract":
    result = math_ops.subtract(num1, num2)
elif operation == "multiply":
    result = math_ops.multiply(num1, num2)
elif operation == "divide":
    result = math_ops.divide(num1, num2)

print(result)
