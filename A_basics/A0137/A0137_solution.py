# A0137 - دومین بزرگترین عدد
# پیدا کردن دومین بزرگترین عدد

n = int(input())
numbers = list(map(int, input().split()))

first = second = float('-inf')

for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(second)
