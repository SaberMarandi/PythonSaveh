# A0112 - مجموع دنباله حسابی
# محاسبه مجموع دنباله حسابی

a, d, n = map(int, input().split())
total = n * (2 * a + (n - 1) * d) // 2
print(total)
