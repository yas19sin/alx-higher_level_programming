#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited from the specified class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
