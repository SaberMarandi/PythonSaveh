# A0103 - مجموع ارقام عدد
# محاسبه مجموع ارقام یک عدد

n = input()
digit_sum = sum(int(digit) for digit in n if digit.isdigit())
print(digit_sum)
