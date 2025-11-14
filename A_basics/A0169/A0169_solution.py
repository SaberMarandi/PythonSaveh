# A0169 - معکوس عدد

n = int(input())
reversed_num = 0
while n > 0:
    reversed_num = reversed_num * 10 + n % 10
    n //= 10
print(reversed_num)
