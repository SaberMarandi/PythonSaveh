# B0016 - دومین بزرگترین عنصر
# پیدا کردن دومین عنصر بزرگ

n = int(input())
numbers = list(map(int, input().split()))
unique = sorted(set(numbers), reverse=True)
print(unique[1])
