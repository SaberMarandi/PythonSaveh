# A0138 - تعداد معکوس‌ها
# شمارش تعداد معکوس‌ها در آرایه

n = int(input())
numbers = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] > numbers[j]:
            count += 1

print(count)
