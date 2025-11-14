# A0151 - تبدیل رشته به عدد

s = input().strip()
result = 0
sign = 1

# بررسی علامت
start = 0
if s[0] == '-':
    sign = -1
    start = 1
elif s[0] == '+':
    start = 1

# تبدیل رشته به عدد
for i in range(start, len(s)):
    if s[i].isdigit():
        result = result * 10 + (ord(s[i]) - ord('0'))
    else:
        break

print(result * sign)
