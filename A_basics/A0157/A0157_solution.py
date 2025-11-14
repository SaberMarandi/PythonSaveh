# A0157 - جذر بدون sqrt

n = int(input())

# روش بابلی برای محاسبه جذر
if n == 0:
    print(0)
else:
    x = n
    while True:
        root = (x + n // x) // 2
        if root >= x:
            print(x)
            break
        x = root
