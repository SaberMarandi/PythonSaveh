# F0004 - استفاده از ماژول random
# تولید اعداد تصادفی

import random

n = int(input())
a = int(input())
b = int(input())

for i in range(n):
    print(random.randint(a, b))
