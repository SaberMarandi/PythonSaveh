# B0002 - جمع عناصر لیست
# محاسبه مجموع عناصر یک لیست

n = int(input())
numbers = list(map(int, input().split()))
total = sum(numbers)
print(total)
