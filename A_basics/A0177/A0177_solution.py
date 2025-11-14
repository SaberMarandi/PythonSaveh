# A0177 - تبدیل به هگزادسیمال

n = int(input())

if n == 0:
    print('0')
else:
    hex_digits = '0123456789ABCDEF'
    result = ''
    
    while n > 0:
        result = hex_digits[n % 16] + result
        n //= 16
    
    print(result)
