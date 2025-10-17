# D0004 - خواندن خط به خط
# خواندن و شماره‌گذاری خطوط

filename = input()
with open(filename, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {line.strip()}")
