# A0139 - چرخش آرایه
# چرخاندن آرایه به راست

n = int(input())
numbers = list(map(int, input().split()))
k = int(input())

k = k % n  # برای جلوگیری از چرخش‌های اضافی
rotated = numbers[-k:] + numbers[:-k]

print(' '.join(map(str, rotated)))
