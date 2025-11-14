# A0172 - بزرگترین رقم

n = int(input())

max_digit = 0
while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n //= 10

print(max_digit)
