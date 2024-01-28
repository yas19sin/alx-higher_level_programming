#!/usr/bin/python3
"""
This is the "3-print_square" module.

The 3-print_square module supplies one function, print_square(size).
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size of the square.

    Raises:
        ValueError: If size is less than 0 or not an integer.
    """
    if not isinstance(size, int) or size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for _ in range(size):
        print("#" * size)
