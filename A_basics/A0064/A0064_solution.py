# A0064 - جمع اعداد طبیعی
# جمع اعداد تا ورود 0

total = 0
while True:
    num = int(input())
    if num == 0:
        break
    total += num
print(total)
