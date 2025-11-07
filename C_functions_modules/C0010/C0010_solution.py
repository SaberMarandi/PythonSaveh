# C0010 - تابع lambda
# مرتب‌سازی با lambda

n = int(input())
numbers = list(map(int, input().split()))

sorted_numbers = sorted(numbers, key=lambda x: x % 5)
print(' '.join(map(str, sorted_numbers)))
