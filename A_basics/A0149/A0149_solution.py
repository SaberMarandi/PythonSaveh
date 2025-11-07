# A0149 - محاسبه توان با الگوریتم سریع
# محاسبه a^b با الگوریتم توان‌رسانی سریع

def fast_power(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result

a, b = map(int, input().split())
print(fast_power(a, b))
