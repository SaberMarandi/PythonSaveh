# A0077 - چاپ الماس ستاره
# چاپ الماس از ستاره‌ها

n = int(input())
mid = n // 2 + 1

# نیمه بالایی
for i in range(1, mid + 1):
    print(' ' * (mid - i) + '*' * (2 * i - 1))

# نیمه پایینی
for i in range(mid - 1, 0, -1):
    print(' ' * (mid - i) + '*' * (2 * i - 1))
