# A0066 - تعداد ارقام فرد
# شمارش ارقام فرد یک عدد

number = input()
count = sum(1 for digit in number if digit.isdigit() and int(digit) % 2 == 1)
print(count)
