from book import Book
from member import Member

class Borrow:
    def __init__(self, borrow_id, member: Member, book: Book):
        self.borrow_id = borrow_id
        self.member = member
        self.book = book

    def borrow_book(self):
        try:
            self.book.borrow_book()
            print(f"Book '{self.book.title}' borrowed by Member '{self.member.name}'")
        except ValueError as e:
            print(e)

    def return_book(self):
        self.book.return_book()
        print(f"Book '{self.book.title}' returned by Member '{self.member.name}'")
