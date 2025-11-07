class Currency:
    exchange_rate = 0
    
    def __init__(self, amount_usd):
        self.amount_usd = amount_usd
    
    def to_rial(self):
        return self.amount_usd * Currency.exchange_rate

# دریافت ورودی
Currency.exchange_rate = float(input())
n = int(input())

for i in range(n):
    amount = float(input())
    currency = Currency(amount)
    print(f"{currency.to_rial():.2f}")
