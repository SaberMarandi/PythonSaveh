class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

# دریافت ورودی
initial = int(input())
deposit_amount = int(input())
withdraw_amount = int(input())

# ایجاد شیء و انجام عملیات
account = BankAccount(initial)
account.deposit(deposit_amount)
account.withdraw(withdraw_amount)
print(account.get_balance())
