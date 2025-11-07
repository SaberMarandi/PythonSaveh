# C0086 - استفاده از map
# به توان 2 رساندن اعداد با map

n = int(input())
numbers = list(map(int, input().split()))

squared = list(map(lambda x: x**2, numbers))
print(' '.join(map(str, squared)))
