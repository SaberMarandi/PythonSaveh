# A0133 - مرتب‌سازی حبابی
# مرتب‌سازی با الگوریتم حبابی

n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(' '.join(map(str, numbers)))
