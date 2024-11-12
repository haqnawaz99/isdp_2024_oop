class Librarian:
    def __init__(self, librarian_id, name):
        self.librarian_id = librarian_id
        self.name = name

    def display_info(self):
        print(f"Librarian ID: {self.librarian_id}, Name: {self.name}")