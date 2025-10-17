# F0003 - ماژول datetime
# نمایش تاریخ و زمان فعلی

from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
