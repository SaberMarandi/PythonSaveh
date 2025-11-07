class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def display(self):
        print(f"فروشگاه: {self.name}")
        print(f"تعداد محصولات: {len(self.products)}")
        for product in self.products:
            print(f"- {product}")

# دریافت ورودی
shop_name = input()
n = int(input())

shop = Shop(shop_name)

for i in range(n):
    product = input()
    shop.add_product(product)

shop.display()
