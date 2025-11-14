# A0188 - بررسی توان 2

n = int(input())

if n > 0 and (n & (n - 1)) == 0:
    print("YES")
else:
    print("NO")
