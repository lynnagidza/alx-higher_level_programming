#!/usr/bin/python3
"""This function prints the last digit of a number.

    Prototype: def print_last_digit(number):
    Returns the value of the last digit
    You are not allowed to import any module
"""


def print_last_digit(number):
    """This function prints the last digit of a number."""
    last_digit = abs(number) % 10
    print(f"{last_digit:d}", end="")
    return last_digit
