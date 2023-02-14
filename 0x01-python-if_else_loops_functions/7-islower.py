#!/usr/bin/python3
"""This function checks for lowercase character.

    Prototype: def islower(c):
    Returns True if c is lowercase
    Returns False otherwise
    You are not allowed to import any module
    You are not allowed to use str.upper() and str.isupper()
"""
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
