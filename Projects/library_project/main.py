from book import Book
from member import Member
from librarian import Librarian
from borrow import Borrow

def main():
    # Create a librarian
    # librarian = Librarian(1, "Mr. Smith")
    # librarian.display_info()

    # Create a book
    book1 = Book("1984", "George Orwell", "123-456-789")
    book2 = Book("Animal Farm", "Zahid", "987-654-321") 
    book2.display_info()

    # Create a member
    member1 = Member(101, "Musa")
    member1.display_info()

    # # Borrow a book
    borrow1 = Borrow(1001, member1, book2)
    borrow1.borrow_book()
    book2.display_info()

    # # Return the book
    # borrow1.return_book()
    # book1.display_info()

# Run the main function
if __name__ == "__main__":
    main()