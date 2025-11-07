# A0093 - مرتب‌سازی اعداد
# مرتب‌سازی لیست اعداد

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
print(' '.join(map(str, numbers)))
