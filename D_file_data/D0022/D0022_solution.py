# D0022 - فیلتر خطوط شروع با کاراکتر
# فیلتر خطوطی که با کاراکتر خاص شروع می‌شوند

input_file = input()
char = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    filtered = [line for line in lines if line.strip().startswith(char)]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(filtered)
    
    print("Filtered successfully")
except FileNotFoundError:
    print("Input file not found")
