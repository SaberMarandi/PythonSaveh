# B0010 - درج عنصر در لیست
# درج عنصر در موقعیت مشخص

n = int(input())
numbers = list(map(int, input().split()))
position = int(input())
value = int(input())
numbers.insert(position, value)
print(numbers)
