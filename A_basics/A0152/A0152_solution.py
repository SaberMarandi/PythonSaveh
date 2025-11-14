# A0152 - تبدیل عدد به رشته

n = int(input())

if n == 0:
    print('0')
else:
    result = ''
    negative = False
    
    if n < 0:
        negative = True
        n = -n
    
    while n > 0:
        digit = n % 10
        result = chr(ord('0') + digit) + result
        n //= 10
    
    if negative:
        result = '-' + result
    
    print(result)
