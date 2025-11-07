class PhoneCall:
    def __init__(self, number, duration, rate):
        self.number = number
        self.duration = duration
        self.rate = rate
    
    def total_cost(self):
        return self.duration * self.rate
    
    def display(self):
        print(f"شماره: {self.number}")
        print(f"مدت: {self.duration} دقیقه")
        print(f"هزینه: {self.total_cost()} تومان")

# دریافت ورودی
number = input()
duration = int(input())
rate = int(input())

# ایجاد شیء و نمایش
call = PhoneCall(number, duration, rate)
call.display()
