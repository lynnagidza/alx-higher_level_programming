#!/usr/bin/python3
"""Write a program that prints numbers from 0 to 99"""
for no in range(0, 100):
    if no == 99:
        print("{:02d}".format(no))
    else:
        print("{:02d}, ".format(no), end="")
