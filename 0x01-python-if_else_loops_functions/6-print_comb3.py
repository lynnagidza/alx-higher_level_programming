#!/usr/bin/python3
"""This program prints all possible combinatins of 2 digits
RULES:
    Numbers must be separated by ,, followed by a space
    The two digits must be different
    01 and 10 are considered the same combination of the two digits 0 and 1
    Print only the smallest combination of two digits
    Numbers should be printed in ascending order, with two digits
    The last number should be followed by a new line
    You can only use no more than 3 print functions with string format
    You can only use no more than 2 loops in your code
    You are not allowed to store numbers or strings in a variable
    You are not allowed to import any module
"""
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
