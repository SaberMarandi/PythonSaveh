# A0121 - الگوی الماس
# چاپ الگوی الماس

n = int(input())

# نیمه بالا
for i in range(n // 2 + 1):
    spaces = ' ' * (n // 2 - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

# نیمه پایین
for i in range(n // 2 - 1, -1, -1):
    spaces = ' ' * (n // 2 - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)
