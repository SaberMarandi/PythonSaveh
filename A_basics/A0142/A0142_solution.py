# A0142 - جابجایی دو عدد بدون متغیر سوم
# جابجایی دو عدد با tuple unpacking

a, b = map(int, input().split())
a, b = b, a
print(b)
print(a)
