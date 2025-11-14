# A0174 - مرتب‌سازی ارقام

n = int(input())

# تبدیل به لیست ارقام
digits = []
temp = n
while temp > 0:
    digits.append(temp % 10)
    temp //= 10

# مرتب‌سازی
digits.sort()

# تبدیل به عدد
result = 0
for digit in digits:
    result = result * 10 + digit

print(result)
