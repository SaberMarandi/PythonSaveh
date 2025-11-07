# D0050 - خواندن فایل خط به خط (بزرگ)
# خواندن فایل بزرگ خط به خط

filename = input()
n = int(input())  # تعداد خطوط اول

try:
    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if i > n:
                break
            print(line.rstrip())
except FileNotFoundError:
    print("File not found")
