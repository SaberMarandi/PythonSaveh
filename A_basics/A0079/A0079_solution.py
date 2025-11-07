# A0079 - چاپ الگوی شطرنجی
# چاپ الگوی شطرنجی

n = int(input())
for i in range(n):
    if i % 2 == 0:
        print('* ' * ((n + 1) // 2))
    else:
        print(' *' * (n // 2))
