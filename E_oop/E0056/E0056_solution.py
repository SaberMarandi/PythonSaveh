class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        return interest

# دریافت ورودی
account_number = input()
balance = float(input())
interest_rate = float(input())

account = SavingsAccount(account_number, balance, interest_rate)
print(f"موجودی اولیه: {account.get_balance():.2f}")

interest = account.add_interest()
print(f"سود: {interest:.2f}")
print(f"موجودی نهایی: {account.get_balance():.2f}")
