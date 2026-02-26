# D0006 - شمارش خطوط فایل
# شمارش تعداد خطوط یک فایل متنی

filename = input()

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(len(lines))
