#!/usr/bin/python3
"""Defines a function that multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list,
            or if m_a or m_b is not a list of lists,
            or if one element of the matrices is not an integer or a float,
            or if the matrices are not rectangular.
        ValueError: If m_a or m_b is empty,
        or if the matrices cannot be multiplied.

    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or \
            not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of "
                        "lists")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row)\
            or not all(
            isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b "
                        "should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a) \
            or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row "
                        "of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b))
               for col_b in zip(*m_b)] for row_a in m_a]

    return result
