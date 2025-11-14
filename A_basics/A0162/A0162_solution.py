# A0162 - بررسی عدد اول با بهینه‌سازی

import math

n = int(input())

if n < 2:
    print("غیر اول")
elif n == 2:
    print("اول")
elif n % 2 == 0:
    print("غیر اول")
else:
    is_prime = True
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("اول")
    else:
        print("غیر اول")
