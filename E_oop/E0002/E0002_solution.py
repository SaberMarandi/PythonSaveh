# E0002 - متد کلاس
# کلاس ماشین حساب

class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
a, b = map(int, input().split())
result = calc.add(a, b)
print(result)
