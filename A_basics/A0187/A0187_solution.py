# A0187 - معکوس بیتها

n = int(input())
result = 0
bits = 32  # فرض کنیم 32 بیت

for i in range(bits):
    if n & (1 << i):
        result |= (1 << (bits - 1 - i))

print(result)
