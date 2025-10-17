# B0009 - حذف عنصر از لیست
# حذف اولین رخداد یک عنصر از لیست

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
if target in numbers:
    numbers.remove(target)
print(numbers)
