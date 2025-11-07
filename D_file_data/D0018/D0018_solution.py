# D0018 - شماره‌گذاری خطوط
# چاپ خطوط فایل با شماره

filename = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines, 1):
            print(f"{i}: {line.rstrip()}")
except FileNotFoundError:
    print("File not found")
