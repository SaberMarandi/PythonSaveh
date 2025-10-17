# B0008 - شمارش تکرار عنصر
# شمارش تعداد تکرار یک عنصر در لیست

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
print(numbers.count(target))
