# A0146 - طول طولانی‌ترین زیررشته بدون تکرار
# پیدا کردن طول طولانی‌ترین زیررشته بدون کاراکتر تکراری

s = input()
char_set = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])
    max_length = max(max_length, right - left + 1)

print(max_length)
