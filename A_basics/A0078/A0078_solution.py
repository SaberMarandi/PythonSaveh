# A0078 - چاپ مربع توخالی
# چاپ مربع توخالی از ستاره‌ها

n = int(input())
for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * n)
    else:
        print('*' + ' ' * (n - 2) + '*')
