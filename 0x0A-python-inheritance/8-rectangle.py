#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle with width and height
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with specified width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle
        """
        return self.__width * self.__height
