# D0012 - شمارش کلمات فایل
# شمارش تعداد کلمات در فایل

filename = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        words = content.split()
        print(len(words))
except FileNotFoundError:
    print(0)
