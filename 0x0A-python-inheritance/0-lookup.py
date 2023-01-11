#!/usr/bin/python3
"""Write a function that returns the list of 
available attributes and methods of an object
"""
def lookup(obj):
    return dir(obj)


class Class1(object):
    pass


class Class2(object):
    attribute1 = 3

    def method1(self):
        pass


# print(lookup(Class1))
print(lookup(Class2))
# print(lookup(int))
