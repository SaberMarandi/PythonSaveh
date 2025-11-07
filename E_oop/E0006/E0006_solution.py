class Calculator:
    def add(self, a, b):
        return a + b

# دریافت ورودی
num1 = int(input())
num2 = int(input())

# ایجاد شیء و محاسبه
calc = Calculator()
result = calc.add(num1, num2)
print(result)
