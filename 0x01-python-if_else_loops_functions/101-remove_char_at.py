#!/usr/bin/python3
"""Module that contains a function that removes the character at position n"""


def remove_char_at(str, n):
    """Returns a copy of the string with the character at position n removed"""
    return str[:n] + str[n+1:]
