# C0071 - استفاده از map()
# محاسبه مربع اعداد با map

n = int(input())
numbers = list(map(int, input().split()))
squares = list(map(lambda x: x**2, numbers))
print(squares)
