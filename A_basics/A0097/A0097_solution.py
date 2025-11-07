# A0097 - حذف تکراری‌ها
# حذف اعداد تکراری از لیست

n = int(input())
numbers = list(map(int, input().split()))
unique = list(dict.fromkeys(numbers))
print(' '.join(map(str, unique)))
