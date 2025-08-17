#Python Magic Methods

#!/usr/bin/env python3

class Book:
    """
    A class to represent a book, demonstrating the use of Python's magic methods.
    """

    def __init__(self, title, author, year):
        """
        Initializes a new Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        This is what is displayed when you use `print()`.
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
        destroyed (garbage collected).
        """
        print(f"Deleting {self.title}")
