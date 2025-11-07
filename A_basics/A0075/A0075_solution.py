# A0075 - چاپ هرم ستاره
# چاپ هرم از ستاره‌ها

n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
