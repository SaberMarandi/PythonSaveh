# A0105 - بررسی عدد آرمسترانگ
# بررسی اینکه آیا عدد آرمسترانگ است

n = input()
num = int(n)
power = len(n)
armstrong_sum = sum(int(digit) ** power for digit in n)

if armstrong_sum == num:
    print("YES")
else:
    print("NO")
