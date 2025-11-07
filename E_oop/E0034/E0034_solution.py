class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return f"{self.name} - قیمت: {self.price} تومان - موجودی: {self.stock}"

# دریافت ورودی
name = input()
price = int(input())
stock = int(input())

# ایجاد شیء و نمایش
product = Product(name, price, stock)
print(product)
