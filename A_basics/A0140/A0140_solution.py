# A0140 - حذف عناصر تکراری از لیست مرتب
# حذف تکراری‌ها از لیست مرتب شده

n = int(input())
numbers = list(map(int, input().split()))

if n == 0:
    print()
else:
    result = [numbers[0]]
    for i in range(1, n):
        if numbers[i] != numbers[i - 1]:
            result.append(numbers[i])
    
    print(' '.join(map(str, result)))
