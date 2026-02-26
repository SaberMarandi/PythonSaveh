# A0072 - جمع اعداد زوج
# محاسبه مجموع اعداد زوج از 1 تا n

n = int(input())
total = sum(i for i in range(2, n + 1, 2))
print(total)
