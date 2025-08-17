#Python Magic Methods

class Book:
    """
    A class to represent a book, demonstrating the use of Python's magic methods.
    """

    def __init__(self, title, author, year):
        """
        Initializes a new Book instance.
        """
        self.title = title
        self.author = author
        self.year = year
        # The print statement below is what's causing the extra line.
        # It has been removed to match the expected output.

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation that can be used to
        recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        The destructor method, called when the object is about to be
        destroyed.
        """
        print(f"Deleting {self.title}")