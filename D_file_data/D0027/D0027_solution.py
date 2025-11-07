# D0027 - یافتن کوتاه‌ترین خط
# پیدا کردن خط با کمترین طول

filename = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    shortest = min(lines, key=len) if lines else ""
    print(shortest)
except FileNotFoundError:
    print("File not found")
