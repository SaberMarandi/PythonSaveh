# A0062 - چاپ اعداد زوج
# چاپ اعداد زوج از 1 تا n

n = int(input())
result = [str(i) for i in range(2, n + 1, 2)]
print(' '.join(result))
