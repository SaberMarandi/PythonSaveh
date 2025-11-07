# D0023 - تبدیل حروف به بزرگ
# تبدیل تمام حروف به uppercase

input_file = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content.upper())
    
    print("Converted successfully")
except FileNotFoundError:
    print("Input file not found")
