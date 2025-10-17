# B0017 - فیلتر کردن لیست
# فیلتر اعداد زوج از لیست

n = int(input())
numbers = list(map(int, input().split()))
result = [x for x in numbers if x % 2 == 0]
print(result)
