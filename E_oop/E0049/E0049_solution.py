class Time:
    def __init__(self, hours, minutes):
        self.__hours = hours
        self.__minutes = minutes
    
    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        if 0 <= value < 24:
            self.__hours = value
    
    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self, value):
        if 0 <= value < 60:
            self.__minutes = value
    
    @property
    def total_minutes(self):
        return self.__hours * 60 + self.__minutes
    
    def display(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}"

# دریافت ورودی
hours = int(input())
minutes = int(input())

time = Time(hours, minutes)
print(f"زمان: {time.display()}")
print(f"کل دقیقه‌ها: {time.total_minutes}")
