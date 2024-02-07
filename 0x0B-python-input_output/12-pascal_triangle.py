#!/usr/bin/python3
"""
Pascal's Triangle module
"""


def pascal_triangle(n):
    """Return Pascal's Triangle up to the nth row"""
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
