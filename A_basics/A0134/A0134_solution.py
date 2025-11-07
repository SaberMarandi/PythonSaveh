# A0134 - مرتب‌سازی انتخابی
# مرتب‌سازی با الگوریتم انتخابی

n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print(' '.join(map(str, numbers)))
