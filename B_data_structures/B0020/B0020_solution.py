# B0020 - تبدیل لیست به رشته
# تبدیل لیست اعداد به رشته

n = int(input())
numbers = list(map(int, input().split()))
result = ' '.join(map(str, numbers))
print(result)
