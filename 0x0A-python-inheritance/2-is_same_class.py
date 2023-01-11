#!/usr/bin/python3
"""Write a function that returns True if the object is exactly an
 instance of the specified class ; otherwise False"""
def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    else:
        return False

a = 2.9
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))