#!/usr/bin/python3
"""
This function prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
"""


def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            print(f"{chr(ord(c) - 32)}", end="")
        else:
            print(f"{c}", end="")
    print()


if __name__ == "__main__":
    uppercase("Hello, World!")
    uppercase("This is a test.")
