# D0025 - فیلتر خطوط حاوی عدد
# فیلتر کردن خطوطی که حاوی عدد هستند

input_file = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    filtered = [line for line in lines if any(char.isdigit() for char in line)]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(filtered)
    
    print("Filtered successfully")
except FileNotFoundError:
    print("Input file not found")
