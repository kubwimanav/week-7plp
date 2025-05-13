class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False
    
    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        return f"{self.title} is already checked out."
    
    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        return f"{self.title} is not checked out."
    
    def get_details(self):
        status = "checked out" if self.checked_out else "available"
        return f"ID: {self.item_id}, Status: {status}"


class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages
    
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Author: {self.author}, Pages: {self.pages}"


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, runtime):
        super().__init__(title, item_id)
        self.director = director
        self.runtime = runtime
    
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Director: {self.director}, Runtime: {self.runtime} minutes"


class AudioBook(LibraryItem):
    def __init__(self, title, item_id, narrator, length):
        super().__init__(title, item_id)
        self.narrator = narrator
        self.length = length
    
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Narrator: {self.narrator}, Length: {self.length} hours"


# Testing the system
book = Book("The Great Gatsby", "B001", "F. Scott Fitzgerald", 180)
dvd = DVD("Inception", "D001", "Christopher Nolan", 148)
audiobook = AudioBook("Dune", "A001", "Scott Brick", 21)

print(book.get_details())
print(book.check_out())
print(book.get_details())

print("\n" + dvd.get_details())
print(dvd.check_out())
print(dvd.return_item())

print("\n" + audiobook.get_details())