# D0034 - حذف کامنت‌ها
# حذف خطوط کامنت از فایل

input_file = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    code_lines = [line for line in lines if not line.strip().startswith('#')]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(code_lines)
    
    print("Comments removed successfully")
except FileNotFoundError:
    print("Input file not found")
