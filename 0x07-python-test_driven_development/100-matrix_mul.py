#!/usr/bin/python3
"""
This is the "100-matrix_mul" module.

The 100-matrix_mul module supplies one function, matrix_mul(m_a, m_b).
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        list: New matrix resulting from the multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists,
                    or if the elements are not integers or floats,
                    or if the matrices are not rectangular.
        ValueError: If m_a or m_b is empty,
        or if the matrices can't be multiplied.
    """
    if not (isinstance(m_a, list) and isinstance(m_b, list)):
        raise TypeError("m_a and m_b must be lists")

    if (not all(isinstance(row, list) for row in m_a)
            or not all(isinstance(row, list) for row in m_b)):
        raise TypeError("m_a and m_b must be lists of lists")

    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")

    if not all(isinstance(val, (int, float)) for row in m_a for val in row) \
            or not all(isinstance(val, (int, float))
                       for row in m_b for val in row):
        raise TypeError("m_a should contain only integers or\
         floats or m_b should contain only integers or floats")

    if (not all(len(row) == len(m_a[0]) for row in m_a)
            or not all(len(row) == len(m_b[0]) for row in m_b)):
        raise TypeError("each row of m_a must be of the same size\
         or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
