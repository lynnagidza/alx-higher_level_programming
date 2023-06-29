#!/usr/bin/python3

"""
101-locked_class module

This module defines the LockedClass that prevents dynamically creating new
instance attributes,
except for 'first_name'.
"""


class LockedClass:
    """LockedClass prevents dynamically creating new instance attributes,
    except for 'first_name'.
    """
    __slots__ = ['first_name']
