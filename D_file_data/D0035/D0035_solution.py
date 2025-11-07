# D0035 - جایگزینی کلمه در فایل
# جایگزینی یک کلمه با کلمه دیگر

input_file = input()
old_word = input()
new_word = input()
output_file = input()

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated_content = content.replace(old_word, new_word)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("Replaced successfully")
except FileNotFoundError:
    print("Input file not found")
