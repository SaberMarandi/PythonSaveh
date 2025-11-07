# D0038 - اندازه فایل
# نمایش اندازه فایل

import os

filename = input()

try:
    size = os.path.getsize(filename)
    print(f"{size} bytes")
except FileNotFoundError:
    print("File not found")
