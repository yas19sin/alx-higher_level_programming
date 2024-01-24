#!/usr/bin/python3
"""Defines a class Square with methods to compute area and compare squares."""


class Square:
    """A square with a size attribute."""
    def __init__(self, size=0):
        """Initialize a Square with a given size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("size must be a non-negative number")
        self.__size = value

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have unequal areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square has a smaller area than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square has a smaller or equal area than the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square has a greater area than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square has a greater or equal area than the other."""
        return self.area() >= other.area()
