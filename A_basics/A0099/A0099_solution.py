# A0099 - معکوس کردن لیست
# معکوس کردن ترتیب اعداد

n = int(input())
numbers = list(map(int, input().split()))
print(' '.join(map(str, numbers[::-1])))
