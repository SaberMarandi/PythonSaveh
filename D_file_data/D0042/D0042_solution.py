# D0042 - حذف پوشه خالی
# حذف یک پوشه خالی

import os

folder = input()

try:
    os.rmdir(folder)
    print("Folder deleted successfully")
except FileNotFoundError:
    print("Folder not found")
except OSError:
    print("Folder is not empty")
except Exception as e:
    print(f"Error: {e}")
