class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}")

    def borrow_book(self):
        if self.available:
            self.available = False
        else:
            raise ValueError("Book is already borrowed!")

    def return_book(self):
        self.available = True