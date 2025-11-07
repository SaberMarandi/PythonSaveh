# A0080 - چاپ الگوی اعداد مثلثی
# چاپ مثلث از اعداد

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
