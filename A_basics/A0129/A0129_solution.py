# A0129 - ترکیب (nCr)
# محاسبه ترکیب با استفاده از فاکتوریل

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n, r = map(int, input().split())
result = factorial(n) // (factorial(r) * factorial(n - r))
print(result)
