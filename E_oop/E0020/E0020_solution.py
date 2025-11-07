class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def display(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

# دریافت ورودی
hour = int(input())
minute = int(input())
second = int(input())

# ایجاد شیء و نمایش
time = Time(hour, minute, second)
print(time.display())
