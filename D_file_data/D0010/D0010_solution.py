# D0010 - بررسی وجود فایل
# بررسی اینکه آیا فایل وجود دارد

import os

filename = input()

if os.path.exists(filename):
    print("YES")
else:
    print("NO")
