# C0005 - پارامتر پیش‌فرض
# محاسبه توان با پارامتر پیش‌فرض

def power(base, exponent=2):
    return base ** exponent

numbers = list(map(int, input().split()))
if len(numbers) == 1:
    result = power(numbers[0])
else:
    result = power(numbers[0], numbers[1])
print(result)
