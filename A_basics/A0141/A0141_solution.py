# A0141 - ادغام دو لیست مرتب
# ادغام دو لیست مرتب شده

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

merged = []
i = j = 0

while i < n and j < m:
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

merged.extend(list1[i:])
merged.extend(list2[j:])

print(' '.join(map(str, merged)))
