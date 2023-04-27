#!/usr/bin/python3
"""This module defines a function that computes a to the power of b."""


def pow(a, b):
    """Compute a to the power of b and return the value."""
    if b == 0:
        return 1
    elif b < 0:
        a = 1 / a
        b = -b
    res = 1
    while b > 0:
        if b % 2 == 1:
            res *= a
        a *= a
        b //= 2
    return res
