# D0011 - جستجوی کلمه در فایل
# شمارش تعداد تکرار یک کلمه در فایل

filename = input()
word = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        count = content.lower().split().count(word.lower())
        print(count)
except FileNotFoundError:
    print(0)
