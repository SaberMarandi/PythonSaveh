# A0131 - جستجوی خطی
# پیدا کردن عدد با جستجوی خطی

n = int(input())
numbers = list(map(int, input().split()))
search = int(input())

index = -1
for i in range(n):
    if numbers[i] == search:
        index = i
        break

print(index)
