# D0005 - افزودن به فایل
# افزودن متن به انتهای فایل

filename = input()
text = input()
with open(filename, 'a', encoding='utf-8') as f:
    f.write(text + '\n')
print("Text appended successfully")
