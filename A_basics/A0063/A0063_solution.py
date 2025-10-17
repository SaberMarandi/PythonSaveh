# A0063 - چاپ اعداد فرد
# چاپ اعداد فرد از 1 تا n

n = int(input())
result = [str(i) for i in range(1, n + 1, 2)]
print(' '.join(result))
