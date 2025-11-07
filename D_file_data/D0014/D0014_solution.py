# D0014 - خواندن خط خاص
# خواندن خط n ام فایل

filename = input()
n = int(input())

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        if 1 <= n <= len(lines):
            print(lines[n - 1].strip())
        else:
            print("Line number out of range")
except FileNotFoundError:
    print("File not found")
