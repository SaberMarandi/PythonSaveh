# A0082 - شمارش حروف صدادار
# شمارش تعداد حروف صدادار در رشته

text = input()
vowels = 'aeiouAEIOU'
count = sum(1 for char in text if char in vowels)
print(count)
