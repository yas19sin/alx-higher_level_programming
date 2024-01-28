#!/usr/bin/python3
"""
This is the "4-text_indentation" module.

The 4-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after ., ? and : characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = [".", "?", ":"]
    start = 0

    for idx, char in enumerate(text):
        if char in separators:
            print(text[start:idx + 1].strip())
            print()
            start = idx + 1

    print(text[start:].strip())
