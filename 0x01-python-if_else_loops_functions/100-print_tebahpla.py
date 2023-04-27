#!/usr/bin/python3
"""
    Prints the ASCII alphabet, in reverse order, alternating lowercase and
    uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
"""


for i in range(ord('z'), ord('a')-1, -1):
    print("{0:c}".format(i if i % 2 == 0 else i - 32), end="")
