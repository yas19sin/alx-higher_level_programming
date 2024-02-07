#!/usr/bin/python3
"""
Write file module
"""


def write_file(filename="", text=""):
    """Write a string to a text file and
        return the number of characters written"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
