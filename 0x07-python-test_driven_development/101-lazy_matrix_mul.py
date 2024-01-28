#!/usr/bin/env python3
"""
Lazy matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Parameters:
        - m_a (list of lists): First matrix
        - m_b (list of lists): Second matrix

    Returns:
        - numpy.ndarray: Resulting matrix
    """
    return np.dot(m_a, m_b)
