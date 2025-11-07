# D0048 - کپی پوشه
# کپی کردن پوشه و محتویات آن

import shutil

source = input()
destination = input()

try:
    shutil.copytree(source, destination)
    print("Folder copied successfully")
except FileNotFoundError:
    print("Source folder not found")
except FileExistsError:
    print("Destination folder already exists")
except Exception as e:
    print(f"Error: {e}")
