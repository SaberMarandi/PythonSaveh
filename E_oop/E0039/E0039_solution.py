class Restaurant:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    def add_order(self, item, price):
        self.orders.append((item, price))
    
    def total(self):
        return sum(price for item, price in self.orders)
    
    def display(self):
        print(f"رستوران: {self.name}")
        print(f"تعداد سفارشات: {len(self.orders)}")
        print(f"مجموع: {self.total()} تومان")

# دریافت ورودی
name = input()
n = int(input())

restaurant = Restaurant(name)

for i in range(n):
    line = input().split()
    item = line[0]
    price = int(line[1])
    restaurant.add_order(item, price)

restaurant.display()
