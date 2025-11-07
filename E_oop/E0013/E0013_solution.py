class Age:
    def __init__(self, age):
        if 0 <= age <= 150:
            self.age = age
            self.valid = True
        else:
            self.valid = False
    
    def display(self):
        if self.valid:
            return f"سن معتبر: {self.age}"
        else:
            return "سن نامعتبر"

# دریافت ورودی
age = int(input())

# ایجاد شیء و نمایش
person_age = Age(age)
print(person_age.display())
