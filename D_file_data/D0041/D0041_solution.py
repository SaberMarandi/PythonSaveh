# D0041 - ایجاد پوشه
# ایجاد یک پوشه جدید

import os

folder = input()

try:
    os.mkdir(folder)
    print("Folder created successfully")
except FileExistsError:
    print("Folder already exists")
except Exception as e:
    print(f"Error: {e}")
