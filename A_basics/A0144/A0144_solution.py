# A0144 - پیدا کردن عنصر گمشده
# پیدا کردن عدد گمشده در دنباله 1 تا n

n = int(input())
numbers = list(map(int, input().split()))

# مجموع اعداد 1 تا n
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

print(expected_sum - actual_sum)
