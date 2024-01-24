#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size,
    size validation, and a method to compute the area."""


class Square:
    """A class Square with a private instance attribute size,
        size validation, and a method to compute the area."""
    def __init__(self, size=0):
        """Set the size of the square with validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2
