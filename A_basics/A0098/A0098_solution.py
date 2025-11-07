# A0098 - تعداد اعداد مثبت و منفی
# شمارش اعداد مثبت و منفی

n = int(input())
numbers = list(map(int, input().split()))
positive = sum(1 for num in numbers if num > 0)
negative = sum(1 for num in numbers if num < 0)
print(positive)
print(negative)
