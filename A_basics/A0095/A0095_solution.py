# A0095 - جمع اعداد فرد
# محاسبه جمع اعداد فرد

n = int(input())
numbers = list(map(int, input().split()))
odd_sum = sum(num for num in numbers if num % 2 != 0)
print(odd_sum)
