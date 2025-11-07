class Invoice:
    def __init__(self, product, unit_price, quantity, tax_rate):
        self.product = product
        self.unit_price = unit_price
        self.quantity = quantity
        self.tax_rate = tax_rate
    
    def subtotal(self):
        return self.unit_price * self.quantity
    
    def tax(self):
        return self.subtotal() * self.tax_rate / 100
    
    def total(self):
        return self.subtotal() + self.tax()
    
    def display(self):
        print(f"محصول: {self.product}")
        print(f"قیمت کل: {int(self.subtotal())}")
        print(f"مالیات: {int(self.tax())}")
        print(f"قیمت نهایی: {int(self.total())}")

# دریافت ورودی
product = input()
unit_price = float(input())
quantity = int(input())
tax_rate = float(input())

# ایجاد شیء و نمایش
invoice = Invoice(product, unit_price, quantity, tax_rate)
invoice.display()
