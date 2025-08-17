# Exploring Polymorphism and Method Overriding

import math

class Shape:
    """
    A base class for geometric shapes.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method must be overridden by derived classes.
        """
        raise NotImplementedError("Subclass must implement abstract method 'area'")

class Rectangle(Shape):
    """
    A class to represent a rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area method to calculate the area of a rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class to represent a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Overrides the area method to calculate the area of a circle.
        """
        return math.pi * (self.radius ** 2)