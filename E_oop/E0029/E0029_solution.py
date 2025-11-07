class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def display(self):
        return f"{self.year}/{self.month}/{self.day}"
    
    def is_equal(self, other):
        return (self.day == other.day and 
                self.month == other.month and 
                self.year == other.year)

# دریافت ورودی
d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

# ایجاد اشیاء
date1 = Date(d1, m1, y1)
date2 = Date(d2, m2, y2)

print(date1.display())
print(date2.display())

if date1.is_equal(date2):
    print("برابر")
else:
    print("نابرابر")
