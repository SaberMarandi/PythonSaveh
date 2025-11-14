# A0156 - توان بدون عملگر **

base = int(input())
exp = int(input())

result = 1
for i in range(exp):
    result *= base

print(result)
