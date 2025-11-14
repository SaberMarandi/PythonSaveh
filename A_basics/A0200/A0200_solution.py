# A0200 - ماشین حساب ساده

num1 = float(input())
operator = input().strip()
num2 = float(input())

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    if num2 == 0:
        print("خطا: تقسیم بر صفر")
    else:
        result = num1 / num2
        print(result)
else:
    print("خطا: عملگر نامعتبر")
