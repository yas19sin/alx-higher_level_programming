#!/usr/bin/python3
"""Defines a class MagicClass that emulates given Python bytecode."""


import math


class MagicClass:
    """A class that emulates given Python bytecode."""
    def __init__(self, radius=0):
        """Initialize a MagicClass with a given radius."""
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
