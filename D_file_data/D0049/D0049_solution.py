# D0049 - حذف پوشه و محتویات
# حذف پوشه به همراه تمام فایل‌ها و زیرپوشه‌ها

import shutil

folder = input()

try:
    shutil.rmtree(folder)
    print("Folder deleted successfully")
except FileNotFoundError:
    print("Folder not found")
except Exception as e:
    print(f"Error: {e}")
