#!/usr/bin/python3
'''defines the base class'''
class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id_=None):
        if id_ is not None:
            self.id_ = id_
        else:
            Base.__nb_objects += 1
            self.id_ = Base.__nb_objects
