# A0096 - میانگین اعداد
# محاسبه میانگین اعداد

n = int(input())
numbers = list(map(int, input().split()))
average = sum(numbers) / n
print(f"{average:.2f}")
