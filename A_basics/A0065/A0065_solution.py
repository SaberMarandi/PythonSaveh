# A0065 - تعداد ارقام زوج
# شمارش ارقام زوج یک عدد

number = input()
count = sum(1 for digit in number if digit.isdigit() and int(digit) % 2 == 0)
print(count)
