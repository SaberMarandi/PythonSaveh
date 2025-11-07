class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, title):
        self.books.append(title)
    
    def display(self):
        print(f"کتابخانه: {self.name}")
        print(f"تعداد کتاب‌ها: {len(self.books)}")
        print("کتاب‌ها:")
        for book in sorted(self.books):
            print(f"- {book}")

# دریافت ورودی
name = input()
n = int(input())

library = Library(name)

for i in range(n):
    title = input()
    library.add_book(title)

library.display()
