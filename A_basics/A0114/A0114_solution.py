# A0114 - اعداد فیبوناچی کمتر از n
# چاپ اعداد فیبوناچی کمتر از n

n = int(input())
fib = []
a, b = 0, 1
while a < n:
    fib.append(a)
    a, b = b, a + b
print(' '.join(map(str, fib)))
