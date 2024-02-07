#!/usr/bin/python3
"""
Module for appending text after
specific lines in a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Append new_string after each line
        containing search_string in the file"""
    with open(filename, 'r') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
    with open(filename, 'w') as f:
        f.writelines(new_lines)
