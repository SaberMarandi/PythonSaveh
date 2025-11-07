# D0045 - لیست فایل‌های پوشه
# نمایش تمام فایل‌های یک پوشه

import os

folder = input()

try:
    items = os.listdir(folder)
    files = [item for item in items if os.path.isfile(os.path.join(folder, item))]
    
    for file in files:
        print(file)
except FileNotFoundError:
    print("Folder not found")
