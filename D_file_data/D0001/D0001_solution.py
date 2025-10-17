# D0001 - خواندن فایل متنی
# خواندن و چاپ محتوای فایل

filename = input()
try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found")
