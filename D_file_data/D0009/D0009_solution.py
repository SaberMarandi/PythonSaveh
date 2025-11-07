# D0009 - تغییر نام فایل
# تغییر نام یک فایل

import os

old_name = input()
new_name = input()

try:
    os.rename(old_name, new_name)
    print("File renamed successfully")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")
