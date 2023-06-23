#!/usr/bin/python3
"""Defines a function that adds two integers."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer. Defaults to 98.

    Returns:
        int: The addition of `a` and `b` as an integer.

    Raises:
        TypeError: If `a` or `b` is not an integer or a float.

    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return int(a + b)
