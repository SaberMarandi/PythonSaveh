class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display(self):
        return f"{self.name}: {self.price} تومان"

class Book(Product):
    def __init__(self, name, price, author, pages):
        super().__init__(name, price)
        self.author = author
        self.pages = pages
    
    def display(self):
        return f"{super().display()}, نویسنده: {self.author}, صفحات: {self.pages}"

class Electronics(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty
    
    def display(self):
        return f"{super().display()}, برند: {self.brand}, گارانتی: {self.warranty} ماه"

# دریافت ورودی
product_type = input()
name = input()
price = float(input())

if product_type == "book":
    author = input()
    pages = int(input())
    product = Book(name, price, author, pages)
elif product_type == "electronics":
    brand = input()
    warranty = int(input())
    product = Electronics(name, price, brand, warranty)

print(product.display())
