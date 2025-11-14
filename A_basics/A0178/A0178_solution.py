# A0178 - تبدیل به اکتال

n = int(input())

if n == 0:
    print('0')
else:
    result = ''
    
    while n > 0:
        result = str(n % 8) + result
        n //= 8
    
    print(result)
