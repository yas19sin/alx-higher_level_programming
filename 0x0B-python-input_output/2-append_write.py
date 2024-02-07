#!/usr/bin/python3
"""
Append to file module
"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file
        and return the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
