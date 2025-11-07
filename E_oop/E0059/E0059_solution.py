class Account:
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

class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return True
        return False

# دریافت ورودی
account_number = input()
balance = float(input())
overdraft_limit = float(input())
withdraw_amount = float(input())

account = CheckingAccount(account_number, balance, overdraft_limit)
print(f"موجودی اولیه: {account.balance:.0f}")

if account.withdraw(withdraw_amount):
    print(f"برداشت موفق")
    print(f"موجودی نهایی: {account.balance:.0f}")
else:
    print(f"برداشت ناموفق")
    print(f"موجودی نهایی: {account.balance:.0f}")
