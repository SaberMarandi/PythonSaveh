# D0016 - شمارش خطوط خالی
# شمارش تعداد خطوط خالی در فایل

filename = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        empty_count = sum(1 for line in lines if line.strip() == '')
        print(empty_count)
except FileNotFoundError:
    print(0)
