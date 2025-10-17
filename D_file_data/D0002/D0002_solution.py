# D0002 - نوشتن در فایل
# نوشتن متن در فایل

filename = input()
text = input()
with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)
print("File written successfully")
