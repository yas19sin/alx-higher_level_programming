#!/usr/bin/python3
"""
This is the "1-matrix_divided" module.

The 1-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): List of lists containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: New matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists, or div is not a number.
        ValueError: If matrix is empty, or if matrix contains invalid elements,
                    or if div is 0.
    """
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix\
         (list of lists) of integers/floats")

    if not matrix or not all(isinstance(val, (int, float))
                             for row in matrix for val in row):
        raise ValueError("matrix can't be empty")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ValueError("division by zero")

    return [[round(val / div, 2) for val in row] for row in matrix]
