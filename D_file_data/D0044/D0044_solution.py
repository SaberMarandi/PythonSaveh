# D0044 - شمارش فایل‌های پوشه
# شمارش تعداد فایل‌ها و پوشه‌ها

import os

path = input()

try:
    items = os.listdir(path)
    files = sum(1 for item in items if os.path.isfile(os.path.join(path, item)))
    folders = sum(1 for item in items if os.path.isdir(os.path.join(path, item)))
    
    print(f"{files} files")
    print(f"{folders} folders")
except FileNotFoundError:
    print("Path not found")
