# C0072 - استفاده از filter()
# فیلتر اعداد زوج

n = int(input())
numbers = list(map(int, input().split()))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
