# A0086 - تبدیل به حروف بزرگ و کوچک
# تبدیل رشته به حروف متناوب بزرگ و کوچک

text = input()
result = ''
for i, char in enumerate(text):
    if i % 2 == 0:
        result += char.upper()
    else:
        result += char.lower()
print(result)
