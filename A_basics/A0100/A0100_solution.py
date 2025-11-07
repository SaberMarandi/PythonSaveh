# A0100 - جستجوی عدد در لیست
# بررسی وجود عدد در لیست

n = int(input())
numbers = list(map(int, input().split()))
search = int(input())

if search in numbers:
    print("YES")
else:
    print("NO")
