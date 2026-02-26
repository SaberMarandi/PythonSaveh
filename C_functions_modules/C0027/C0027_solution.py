# C0027 - تابع بررسی زوج/فرد
# بررسی زوج یا فرد بودن عدد

def is_even(n):
    return n % 2 == 0

n = int(input())
print("Even" if is_even(n) else "Odd")
