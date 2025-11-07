# A0147 - تبدیل رومی به عدد
# تبدیل عدد رومی به عدد صحیح

roman = input()

values = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

result = 0
for i in range(len(roman)):
    if i + 1 < len(roman) and values[roman[i]] < values[roman[i + 1]]:
        result -= values[roman[i]]
    else:
        result += values[roman[i]]

print(result)
