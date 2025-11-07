class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

# دریافت ورودی
title = input()
author = input()

# ایجاد شیء و نمایش
book = Book(title, author)
print(str(book))
print(repr(book))
