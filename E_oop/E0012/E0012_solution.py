class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# دریافت ورودی
n = int(input())

# ایجاد اشیاء
for i in range(n):
    obj = Counter()

print(Counter.get_count())
