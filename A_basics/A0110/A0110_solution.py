# A0110 - بررسی عدد کامل
# بررسی اینکه آیا عدد کامل است

n = int(input())
divisors_sum = sum(i for i in range(1, n) if n % i == 0)

if divisors_sum == n:
    print("YES")
else:
    print("NO")
