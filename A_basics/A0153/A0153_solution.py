# A0153 - بررسی عدد زوج یا فرد بدون modulo

n = int(input())

# استفاده از عملیات بیتی
if n & 1 == 0:
    print("زوج")
else:
    print("فرد")
