# B0022 - حذف تکراری از لیست
# حذف عناصر تکراری و نگه‌داشتن عناصر یکتا

numbers = list(map(int, input().split()))
unique = list(set(numbers))
print(*unique)
