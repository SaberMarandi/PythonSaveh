# D0017 - حذف خطوط خالی
# حذف خطوط خالی از فایل

input_file = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    non_empty_lines = [line for line in lines if line.strip() != '']
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(non_empty_lines)
    
    print("Empty lines removed successfully")
except FileNotFoundError:
    print("Input file not found")
