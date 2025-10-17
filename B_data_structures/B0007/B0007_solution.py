# B0007 - جستجوی عنصر در لیست
# بررسی وجود عنصر در لیست

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
if target in numbers:
    print("Found")
else:
    print("Not Found")
