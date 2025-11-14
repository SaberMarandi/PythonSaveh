# A0180 - بررسی آناگرام

def are_anagrams(str1, str2):
    # حذف فاصله‌ها و تبدیل به حروف کوچک
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # اگر طول‌ها متفاوت باشند، anagram نیستند
    if len(str1) != len(str2):
        return False
    
    # مرتب‌سازی حروف و مقایسه
    return sorted(str1) == sorted(str2)

str1 = input().strip()
str2 = input().strip()

if are_anagrams(str1, str2):
    print("YES")
else:
    print("NO")
