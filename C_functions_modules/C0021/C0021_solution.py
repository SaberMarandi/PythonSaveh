# C0021 - استفاده از *args
# جمع تعداد نامحدود عدد

def sum_all(*args):
    return sum(args)

numbers = list(map(int, input().split()))
result = sum_all(*numbers)
print(result)
