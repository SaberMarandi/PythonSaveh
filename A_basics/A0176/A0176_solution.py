# A0176 - تبدیل به باینری

n = int(input())

if n == 0:
    print('0')
else:
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    print(binary)

# یا می‌توان از تابع داخلی استفاده کرد:
# print(bin(n)[2:])
