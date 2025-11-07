# D0047 - فایل‌های با پسوند خاص
# لیست فایل‌های با پسوند مشخص

import os

folder = input()
extension = input()

try:
    items = os.listdir(folder)
    files = [item for item in items if item.endswith(extension) and os.path.isfile(os.path.join(folder, item))]
    
    for file in files:
        print(file)
except FileNotFoundError:
    print("Folder not found")
