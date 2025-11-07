# D0031 - جایگزینی با regex
# جایگزینی اعداد با کلمه NUMBER

import re

input_file = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = re.sub(r'\d+', 'NUMBER', content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(updated)
    
    print("Replaced successfully")
except FileNotFoundError:
    print("Input file not found")
