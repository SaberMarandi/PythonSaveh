# D0026 - یافتن طولانی‌ترین خط
# پیدا کردن خط با بیشترین طول

filename = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    longest = max(lines, key=len) if lines else ""
    print(longest.strip())
except FileNotFoundError:
    print("File not found")
