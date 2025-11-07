class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        return f"عنوان: {self.title}, نویسنده: {self.author}, سال: {self.year}"

# دریافت ورودی
title = input()
author = input()
year = int(input())

# ایجاد شیء و نمایش اطلاعات
book = Book(title, author, year)
print(book.display_info())
