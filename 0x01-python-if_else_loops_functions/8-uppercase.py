#!/usr/bin/python3
"""
This module defines a function that prints a string in uppercase.
"""


def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        diff = ord('A') - ord('a')
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(ord(c) + diff)
        print("{:s}".format(c), end="")
    print("")


if __name__ == "__main__":
    uppercase("Hello, World!")
