# D0051 - جستجو در فایل
# شمارش تکرار کلمه در فایل

filename = input()
word = input()

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()
    words = content.lower().split()
    count = words.count(word.lower())
    print(count)
