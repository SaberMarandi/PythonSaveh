class Vehicle:
    def __init__(self, name, distance, fuel):
        self.name = name
        self.distance = distance
        self.fuel = fuel
    
    def fuel_efficiency(self):
        return self.distance / self.fuel
    
    def display(self):
        print(f"وسیله: {self.name}")
        print(f"میانگین مصرف: {self.fuel_efficiency():.2f} کیلومتر به ازای هر لیتر")

# دریافت ورودی
name = input()
distance = float(input())
fuel = float(input())

# ایجاد شیء و نمایش
vehicle = Vehicle(name, distance, fuel)
vehicle.display()
