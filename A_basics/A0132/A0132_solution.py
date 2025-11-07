# A0132 - جستجوی دودویی
# پیدا کردن عدد با جستجوی دودویی

n = int(input())
numbers = list(map(int, input().split()))
search = int(input())

left, right = 0, n - 1
index = -1

while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == search:
        index = mid
        break
    elif numbers[mid] < search:
        left = mid + 1
    else:
        right = mid - 1

print(index)
