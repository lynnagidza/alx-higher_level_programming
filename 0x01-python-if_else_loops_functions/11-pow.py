#!/usr/bin/python3
"""This module defines a function that computes a to the power of b."""


def pow(a, b):
    """Compute a to the power of b and return the value."""
    res = 1
    for i in range(b):
        res *= a
    return res
