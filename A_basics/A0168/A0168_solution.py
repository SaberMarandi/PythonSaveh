# A0168 - اعداد آرمسترانگ

n = int(input())
original = n
digits = len(str(n))
sum_powers = 0

while n > 0:
    digit = n % 10
    sum_powers += digit ** digits
    n //= 10

if sum_powers == original:
    print("Armstrong")
else:
    print("Not Armstrong")
