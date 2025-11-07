# D0043 - لیست پوشه‌ها
# نمایش تمام پوشه‌های یک مسیر

import os

path = input()

try:
    items = os.listdir(path)
    folders = [item for item in items if os.path.isdir(os.path.join(path, item))]
    
    for folder in folders:
        print(folder)
except FileNotFoundError:
    print("Path not found")
