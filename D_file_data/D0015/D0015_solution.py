# D0015 - جستجوی خط حاوی کلمه
# پیدا کردن خطوط حاوی کلمه خاص

filename = input()
word = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        found = False
        for line in lines:
            if word.lower() in line.lower():
                print(line.strip())
                found = True
        if not found:
            print("No lines found")
except FileNotFoundError:
    print("File not found")
