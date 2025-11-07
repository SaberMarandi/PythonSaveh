# D0030 - مرتب‌سازی خطوط فایل
# مرتب‌سازی خطوط به ترتیب الفبایی

input_file = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    sorted_lines = sorted(lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(sorted_lines)
    
    print("Lines sorted successfully")
except FileNotFoundError:
    print("Input file not found")
