# D0013 - شمارش کاراکترها
# شمارش تعداد کاراکترها بدون فاصه

filename = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        chars = content.replace(' ', '').replace('\n', '').replace('\t', '')
        print(len(chars))
except FileNotFoundError:
    print(0)
