# B0018 - ضرب عناصر لیست
# محاسبه حاصل‌ضرب همه عناصر

n = int(input())
numbers = list(map(int, input().split()))
result = 1
for num in numbers:
    result *= num
print(result)
