class BMI:
    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
    
    @property
    def bmi(self):
        return self.__weight / (self.__height ** 2)
    
    @property
    def category(self):
        bmi_value = self.bmi
        if bmi_value < 18.5:
            return "کم‌وزن"
        elif bmi_value < 25:
            return "نرمال"
        elif bmi_value < 30:
            return "اضافه‌وزن"
        else:
            return "چاق"

# دریافت ورودی
weight = float(input())
height = float(input())

bmi = BMI(weight, height)
print(f"وزن: {bmi.weight} کیلوگرم")
print(f"قد: {bmi.height} متر")
print(f"BMI: {bmi.bmi:.2f}")
print(f"دسته‌بندی: {bmi.category}")
