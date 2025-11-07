# D0039 - تاریخ آخرین تغییر
# نمایش تاریخ آخرین تغییر فایل

import os
from datetime import datetime

filename = input()

try:
    mtime = os.path.getmtime(filename)
    dt = datetime.fromtimestamp(mtime)
    print(dt.strftime('%Y-%m-%d %H:%M:%S'))
except FileNotFoundError:
    print("File not found")
