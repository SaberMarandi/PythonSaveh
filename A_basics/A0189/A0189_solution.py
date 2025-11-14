# A0189 - نزدیکترین توان 2

n = int(input())

# پیدا کردن بزرگترین توان 2 کمتر یا مساوی n
power = 1
while power <= n:
    power *= 2
power //= 2

# بررسی کدام نزدیک‌تر است
next_power = power * 2

if abs(n - power) <= abs(n - next_power):
    print(power)
else:
    print(next_power)
