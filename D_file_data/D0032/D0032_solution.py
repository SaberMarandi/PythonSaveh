# D0032 - استخراج ایمیل‌ها
# پیدا کردن تمام آدرس‌های ایمیل

import re

filename = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    emails = re.findall(r'\S+@\S+', content)
    
    for email in emails:
        print(email)
except FileNotFoundError:
    print("File not found")
