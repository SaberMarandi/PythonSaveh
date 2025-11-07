# D0036 - ترکیب چند فایل
# ترکیب محتوای چند فایل

n = int(input())
files = [input() for _ in range(n)]
output_file = input()

try:
    with open(output_file, 'w', encoding='utf-8') as out:
        for file in files:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    out.write(f.read())
                    out.write('\n')
            except FileNotFoundError:
                print(f"Warning: {file} not found")
    
    print("Files combined successfully")
except Exception as e:
    print(f"Error: {e}")
