# D0028 - حذف خطوط تکراری
# حذف خطوط تکراری از فایل

input_file = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    unique_lines = list(dict.fromkeys(lines))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(unique_lines)
    
    print("Duplicates removed successfully")
except FileNotFoundError:
    print("Input file not found")
