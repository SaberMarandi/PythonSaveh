# A0159 - باقیمانده بدون modulo

a = int(input())
b = int(input())

# محاسبه باقیمانده بدون %
quotient = a // b
remainder = a - (quotient * b)

print(remainder)
