# A0136 - بزرگترین زیرآرایه
# الگوریتم کادین برای پیدا کردن بزرگترین مجموع زیرآرایه

n = int(input())
numbers = list(map(int, input().split()))

max_sum = numbers[0]
current_sum = numbers[0]

for i in range(1, n):
    current_sum = max(numbers[i], current_sum + numbers[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)
