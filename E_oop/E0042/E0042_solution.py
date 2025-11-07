class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("موجودی نمی‌تواند منفی باشد")

# دریافت ورودی
initial = int(input())
account = BankAccount(initial)

n = int(input())
for i in range(n):
    new_balance = int(input())
    account.set_balance(new_balance)

print(account.get_balance())
