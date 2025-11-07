# D0033 - حذف فاصله‌های اضافی
# حذف فاصه‌های متوالی

import re

input_file = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cleaned = re.sub(r' +', ' ', content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    
    print("Spaces removed successfully")
except FileNotFoundError:
    print("Input file not found")
