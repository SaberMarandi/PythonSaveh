# B0025 - شمارش تکرار
# شمارش تعداد تکرار هر عنصر

numbers = list(map(int, input().split()))
from collections import Counter

counts = Counter(numbers)
for num, count in sorted(counts.items()):
    print(f"{num}: {count}")
