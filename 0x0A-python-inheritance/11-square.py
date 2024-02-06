#!/usr/bin/python3
"""
Defines a class Square that inherits
from Rectangle (9-rectangle.py) (task based on 10-square.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square with equal sides
    """

    def __init__(self, size):
        """
        Initializes a square with specified size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
