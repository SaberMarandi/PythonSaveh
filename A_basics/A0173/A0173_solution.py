# A0173 - کوچکترین رقم

n = int(input())

min_digit = 9
while n > 0:
    digit = n % 10
    if digit < min_digit:
        min_digit = digit
    n //= 10

print(min_digit)
