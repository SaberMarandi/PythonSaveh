class User:
    next_id = 1
    
    def __init__(self, name):
        self.id = User.next_id
        self.name = name
        User.next_id += 1
    
    def display(self):
        return f"ID: {self.id}, نام: {self.name}"

# دریافت ورودی
n = int(input())

for i in range(n):
    name = input()
    user = User(name)
    print(user.display())
