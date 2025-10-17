# B0013 - حذف تکراری‌ها
# حذف عناصر تکراری از لیست

n = int(input())
numbers = list(map(int, input().split()))
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(result)
