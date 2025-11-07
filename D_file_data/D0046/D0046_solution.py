# D0046 - جستجوی فایل در پوشه
# بررسی وجود فایل در پوشه

import os

folder = input()
filename = input()

path = os.path.join(folder, filename)

if os.path.exists(path) and os.path.isfile(path):
    print("YES")
else:
    print("NO")
