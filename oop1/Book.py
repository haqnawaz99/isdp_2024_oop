class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

book1 = Book("Python", "Nadeem", 300, 29.99)
print(book1.title)

book2 = Book("Introduction to Data Science", "Shahid", 400, 39.99)
print(book2.author)
