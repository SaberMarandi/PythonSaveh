# A0094 - جمع اعداد زوج
# محاسبه جمع اعداد زوج

n = int(input())
numbers = list(map(int, input().split()))
even_sum = sum(num for num in numbers if num % 2 == 0)
print(even_sum)
