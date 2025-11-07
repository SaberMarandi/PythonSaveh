class SimpleCounter:
    def __init__(self, value=0):
        self.value = value
    
    def increment(self):
        self.value += 1
    
    def decrement(self):
        self.value -= 1
    
    def get_value(self):
        return self.value

# دریافت ورودی
initial = int(input())
inc_count = int(input())
dec_count = int(input())

# ایجاد شیء و انجام عملیات
counter = SimpleCounter(initial)

for i in range(inc_count):
    counter.increment()

for i in range(dec_count):
    counter.decrement()

print(counter.get_value())
