# A0088 - تکرار هر کاراکتر
# تکرار هر کاراکتر n بار

text = input()
n = int(input())
result = ''.join(char * n for char in text)
print(result)
