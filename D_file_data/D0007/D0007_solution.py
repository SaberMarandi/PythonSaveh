# D0007 - کپی فایل
# کپی کردن یک فایل به فایل دیگر

import shutil

source = input()
destination = input()

try:
    shutil.copy(source, destination)
    print("File copied successfully")
except FileNotFoundError:
    print("Source file not found")
except Exception as e:
    print(f"Error: {e}")
