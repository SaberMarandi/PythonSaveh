# C0007 - تابع با پارامتر پیش‌فرض
# محاسبه مساحت مستطیل یا مربع

def area(length, width=None):
    if width is None:
        width = length
    return length * width

length = int(input())
try:
    width = int(input())
    print(area(length, width))
except:
    print(area(length))
