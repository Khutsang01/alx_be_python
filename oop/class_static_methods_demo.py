# Distinguishing Between Class Methods and Static Methods


class Calculator:
    """A simple calculator class demonstrating class and static methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        It does not depend on the class or an instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that returns the product of two numbers.
        It has access to class attributes via the `cls` parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b