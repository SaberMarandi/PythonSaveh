# A0122 - فاکتوریل با بازگشت
# محاسبه فاکتوریل با استفاده از بازگشت

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))
