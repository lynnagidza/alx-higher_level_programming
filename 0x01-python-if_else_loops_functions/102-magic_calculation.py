#!/usr/bin/python3
"""Module that contains a function that does exactly the same as bytecode
in task 102."""


def magic_calculation(a, b, c):
    """Does exactly the same as bytecode in task 102."""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
