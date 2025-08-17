# Mastering Inheritance and Composition in Python


class Book:
    """A base class to represent a general book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    """A class representing an electronic book, inheriting from Book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    """A class representing a physical book, inheriting from Book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """
    A class to represent a library, demonstrating composition by holding a
    collection of book objects.
    """
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book object to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of each book in the library, handling different
        book types.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")