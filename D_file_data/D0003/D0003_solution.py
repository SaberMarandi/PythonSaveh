# D0003 - شمارش خطوط فایل
# شمارش تعداد خطوط

filename = input()
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(len(lines))
