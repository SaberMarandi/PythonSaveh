# B0014 - اشتراک دو لیست
# پیدا کردن عناصر مشترک دو لیست

n1 = int(input())
list1 = list(map(int, input().split()))
n2 = int(input())
list2 = list(map(int, input().split()))
common = list(set(list1) & set(list2))
print(sorted(common))
