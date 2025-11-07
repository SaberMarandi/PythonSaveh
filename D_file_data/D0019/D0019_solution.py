# D0019 - معکوس کردن خطوط فایل
# معکوس کردن ترتیب خطوط

input_file = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    reversed_lines = lines[::-1]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(reversed_lines)
    
    print("Lines reversed successfully")
except FileNotFoundError:
    print("Input file not found")
