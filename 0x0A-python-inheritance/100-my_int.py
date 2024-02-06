#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int
"""


class MyInt(int):
    """
    Represents an integer with inverted == and != operators
    """

    def __eq__(self, other):
        """
        Overrides the equality operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator
        """
        return super().__eq__(other)
