#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size,
size validation, and methods to compute the area and print the square."""


class Square:
    """A class Square with a private instance attribute size,
        size validation, and methods to compute the area
        and print the square."""
    def __init__(self, size=0):
        """Initializes a Square with a given size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
