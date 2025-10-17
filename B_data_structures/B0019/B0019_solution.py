# B0019 - چرخش لیست
# چرخش لیست به اندازه k

n = int(input())
numbers = list(map(int, input().split()))
k = int(input())
k = k % n
result = numbers[k:] + numbers[:k]
print(result)
