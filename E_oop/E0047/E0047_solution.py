class Product:
    def __init__(self, name, price, discount):
        self.__name = name
        self.__price = price
        self.__discount = discount
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
    
    @property
    def discount(self):
        return self.__discount
    
    @discount.setter
    def discount(self, value):
        if 0 <= value <= 100:
            self.__discount = value
    
    @property
    def final_price(self):
        return self.__price * (1 - self.__discount / 100)

# دریافت ورودی
name = input()
price = float(input())
discount = float(input())

product = Product(name, price, discount)
print(f"محصول: {product.name}")
print(f"قیمت: {product.price}")
print(f"تخفیف: {product.discount}%")
print(f"قیمت نهایی: {product.final_price:.2f}")
