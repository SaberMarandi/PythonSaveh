class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    def get_celsius(self):
        return self.__celsius
    
    def set_celsius(self, celsius):
        self.__celsius = celsius
    
    def get_fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    
    def set_fahrenheit(self, fahrenheit):
        self.__celsius = (fahrenheit - 32) * 5/9

# دریافت ورودی
celsius = float(input())
temp = Temperature(celsius)

print(f"سلسیوس: {temp.get_celsius():.2f}")
print(f"فارنهایت: {temp.get_fahrenheit():.2f}")

fahrenheit = float(input())
temp.set_fahrenheit(fahrenheit)

print(f"سلسیوس: {temp.get_celsius():.2f}")
print(f"فارنهایت: {temp.get_fahrenheit():.2f}")
