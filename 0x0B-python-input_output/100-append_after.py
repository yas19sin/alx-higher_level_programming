#!/usr/bin/python3
"""
Search and update module
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a specific string"""
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)
        file.seek(0)
        file.truncate()
        file.writelines(lines)
