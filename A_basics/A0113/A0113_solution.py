# A0113 - مجموع دنباله هندسی
# محاسبه مجموع دنباله هندسی

a, r, n = map(int, input().split())
if r == 1:
    total = a * n
else:
    total = a * (r ** n - 1) // (r - 1)
print(total)
