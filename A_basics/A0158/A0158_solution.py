# A0158 - گرد کردن بدون round

n = float(input())

# گرد کردن دستی
if n >= 0:
    result = int(n + 0.5)
else:
    result = int(n - 0.5)

print(result)
