# A0167 - اعداد کامل

n = int(input())

if n <= 1:
    print("ناکامل")
else:
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    
    if divisors_sum == n:
        print("کامل")
    else:
        print("ناکامل")
