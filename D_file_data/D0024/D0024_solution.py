# D0024 - شمارش تکرار کلمات
# شمارش فراوانی هر کلمه

filename = input()

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().lower()
        words = content.split()
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    for word in sorted(word_count.keys()):
        print(f"{word}: {word_count[word]}")
except FileNotFoundError:
    print("File not found")
