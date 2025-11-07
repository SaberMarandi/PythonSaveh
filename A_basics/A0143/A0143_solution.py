# A0143 - پیدا کردن عنصر اکثریت
# پیدا کردن عنصری که بیش از n/2 بار تکرار شده

n = int(input())
numbers = list(map(int, input().split()))

# الگوریتم Boyer-Moore Voting
candidate = None
count = 0

for num in numbers:
    if count == 0:
        candidate = num
    count += 1 if num == candidate else -1

# بررسی اینکه آیا candidate واقعا اکثریت است
if numbers.count(candidate) > n // 2:
    print(candidate)
else:
    print(-1)
