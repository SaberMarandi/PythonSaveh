# D0008 - حذف فایل
# حذف یک فایل

import os

filename = input()

try:
    os.remove(filename)
    print("File deleted successfully")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")
