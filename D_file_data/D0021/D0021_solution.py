# D0021 - فیلتر خطوط بلندتر از n
# فیلتر کردن خطوط بر اساس طول

input_file = input()
n = int(input())
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    filtered = [line for line in lines if len(line.strip()) > n]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(filtered)
    
    print("Filtered successfully")
except FileNotFoundError:
    print("Input file not found")
