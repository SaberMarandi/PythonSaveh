# D0029 - شمارش خطوط حاوی کلمه
# شمارش تعداد خطوط حاوی کلمه خاص

filename = input()
word = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        count = sum(1 for line in lines if word.lower() in line.lower())
        print(count)
except FileNotFoundError:
    print(0)
