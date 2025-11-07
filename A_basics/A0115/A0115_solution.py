# A0115 - بررسی عدد فیبوناچی
# بررسی اینکه آیا عدد فیبوناچی است

n = int(input())
a, b = 0, 1
is_fib = False

if n == 0 or n == 1:
    is_fib = True
else:
    while b < n:
        a, b = b, a + b
    if b == n:
        is_fib = True

print("YES" if is_fib else "NO")
