# B0015 - اختلاف دو لیست
# پیدا کردن عناصر موجود در لیست اول که در دوم نیستند

n1 = int(input())
list1 = list(map(int, input().split()))
n2 = int(input())
list2 = list(map(int, input().split()))
difference = list(set(list1) - set(list2))
print(sorted(difference))
