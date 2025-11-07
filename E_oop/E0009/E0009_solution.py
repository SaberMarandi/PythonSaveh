class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def get_balance(self):
        return self.balance

# دریافت ورودی
initial_balance = int(input())
deposit_amount = int(input())
withdraw_amount = int(input())

# ایجاد شیء و انجام عملیات
account = BankAccount(initial_balance)
account.deposit(deposit_amount)
account.withdraw(withdraw_amount)
print(account.get_balance())
