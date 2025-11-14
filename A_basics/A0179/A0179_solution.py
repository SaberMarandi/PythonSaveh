# A0179 - تبدیل از باینری

binary = input().strip()
result = 0
power = 0

# از راست به چپ پردازش کنیم
for i in range(len(binary) - 1, -1, -1):
    if binary[i] == '1':
        result += 2 ** power
    power += 1

print(result)
