# A0148 - تبدیل عدد به رومی
# تبدیل عدد صحیح به عدد رومی

n = int(input())

values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

result = ""
for i in range(len(values)):
    count = n // values[i]
    if count:
        result += symbols[i] * count
        n -= values[i] * count

print(result)
