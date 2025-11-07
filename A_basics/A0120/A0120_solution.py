# A0120 - تجزیه به عوامل اول
# تجزیه عدد به عوامل اول

n = int(input())
factors = []
d = 2

while d * d <= n:
    while n % d == 0:
        factors.append(d)
        n //= d
    d += 1

if n > 1:
    factors.append(n)

print(' '.join(map(str, factors)))
