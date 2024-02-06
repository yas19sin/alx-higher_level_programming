#!/usr/bin/python3
"""
Defines a class BaseGeometry with an integer validator method
"""


class BaseGeometry:
    """
    Represents a base geometry class with an integer validator method
    """

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer greater than 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
