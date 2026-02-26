# D0007 - خواندن فایل
# خواندن و چاپ محتوای فایل

filename = input()

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

print(content)
