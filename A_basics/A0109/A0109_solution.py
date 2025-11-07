# A0109 - حاصل‌ضرب ارقام عدد
# محاسبه حاصل‌ضرب ارقام

n = input()
product = 1
for digit in n:
    if digit.isdigit():
        product *= int(digit)
print(product)
