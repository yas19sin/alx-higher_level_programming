#!/usr/bin/python3
"""
Defines a class MyList that inherits from list
"""


class MyList(list):
    """
    Represents a custom list that inherits from the built-in list class
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order
        """
        print(sorted(self))
