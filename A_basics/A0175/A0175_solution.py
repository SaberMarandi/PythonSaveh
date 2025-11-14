# A0175 - حذف صفرهای ابتدایی

s = input().strip()

# حذف صفرهای ابتدایی
result = s.lstrip('0')

# اگر رشته خالی شد، یعنی همه صفر بودند
if not result:
    result = '0'

print(result)
