# C0028 - تابع فاکتوریل بازگشتی
# محاسبه فاکتوریل به صورت بازگشتی

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))
