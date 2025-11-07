# D0006 - خواندن تمام خطوط فایل
# شمارش تعداد خطوط فایل

filename = input()
try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(len(lines))
except FileNotFoundError:
    print("فایل پیدا نشد")
