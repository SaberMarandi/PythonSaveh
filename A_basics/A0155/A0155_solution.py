# A0155 - قدر مطلق بدون abs

n = int(input())

# روش بیتی برای محاسبه قدر مطلق
mask = n >> 31
result = (n + mask) ^ mask

print(result)
