#!/usr/bin/python3
"""
100-magic_string module
This module provides a function to generate a string 'BestSchool' based on the
iteration count.
"""


def magic_string():
    """Returns a string 'BestSchool' n times based on the iteration count."""
    magic_string.count += 1
    return 'BestSchool' * magic_string.count


magic_string.count = -1
