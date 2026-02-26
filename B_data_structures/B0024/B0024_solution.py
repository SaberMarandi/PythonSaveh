# B0024 - پیدا کردن عنصر
# بررسی وجود عنصر در لیست

numbers = list(map(int, input().split()))
x = int(input())

print("Yes" if x in numbers else "No")
