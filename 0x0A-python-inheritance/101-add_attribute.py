#!/usr/bin/python3
"""
Defines a function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to obj with the specified name and value
    Raises a TypeError if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
