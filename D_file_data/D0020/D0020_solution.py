# D0020 - ادغام دو فایل
# ترکیب محتوای دو فایل

file1 = input()
file2 = input()
output_file = input()

try:
    with open(file1, 'r', encoding='utf-8') as f1:
        content1 = f1.read()
    
    with open(file2, 'r', encoding='utf-8') as f2:
        content2 = f2.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content1)
        f.write('\n')
        f.write(content2)
    
    print("Files merged successfully")
except FileNotFoundError as e:
    print(f"File not found: {e}")
