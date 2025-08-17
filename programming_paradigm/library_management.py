#  Implementing Basic OOP for a Library Management System



class Book:
    """A class to represent a book with a title, author, and availability status."""
    
    def __init__(self, title, author):
        """Initializes a new Book instance."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

class Library:
    """A class to manage a collection of books."""

    def __init__(self):
        """Initializes a new Library instance with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by its title.
        If the book is found and available, it is marked as checked out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """
        Returns a book by its title.
        If the book is found and checked out, it is marked as available.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not found or was already available.")

    def list_available_books(self):
        """Prints a list of all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
