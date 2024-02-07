#!/usr/bin/python3
"""
Read file module
"""


def read_file(filename=""):
    """Read a text file and print its content to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
