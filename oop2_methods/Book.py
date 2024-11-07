# Adding basic functions to the Book class and demonstrating how to call them

# Step 1: Define the Book class with additional methods
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
    # Method to display book information
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Price: ${self.price}")
    
    # Method to apply a discount to the book price
    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)
        print(f"Discount applied! New price of '{self.title}' is ${self.price:.2f}")

# Step 2: Create instances of Book and call the methods
book1 = Book("Python", "Nadeem", 300, 29.99)
book2 = Book("Introduction to Data Science", "Shahid", 400, 39.99)

# Step 3: Call the display_info method to show book details
book1.display_info()
book2.display_info()

# Step 4: Apply discount to a book and call display_info again
book1.apply_discount(10)  # Apply 10% discount to book1
book1.display_info()

