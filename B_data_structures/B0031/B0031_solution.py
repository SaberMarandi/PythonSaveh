# B0031 - ایجاد دیکشنری
# دریافت 3 جفت کلید-مقدار و ایجاد دیکشنری

data = {}
for i in range(3):
    key, value = input().split()
    data[key] = value
print(data)
