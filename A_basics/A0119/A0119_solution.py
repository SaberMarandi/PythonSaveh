# A0119 - اعداد اول دوقلو
# پیدا کردن اعداد اول دوقلو

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(2, n - 2):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)
