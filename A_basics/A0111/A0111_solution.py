# A0111 - دنباله فیبوناچی تا n
# چاپ n عدد اول فیبوناچی

n = int(input())
fib = []
a, b = 0, 1
for i in range(n):
    fib.append(a)
    a, b = b, a + b
print(' '.join(map(str, fib)))
