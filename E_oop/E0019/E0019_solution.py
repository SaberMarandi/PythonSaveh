class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount
    
    def final_price(self):
        return self.price - (self.price * self.discount / 100)

# دریافت ورودی
name = input()
price = float(input())
discount = float(input())

# ایجاد شیء و محاسبه
product = Product(name, price, discount)
print(f"{product.final_price():.2f}")
