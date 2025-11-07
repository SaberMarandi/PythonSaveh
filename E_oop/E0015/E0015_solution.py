class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

# دریافت ورودی
celsius = float(input())

# ایجاد شیء و تبدیل
temp = Temperature(celsius)
print(f"{temp.to_fahrenheit():.2f}")
