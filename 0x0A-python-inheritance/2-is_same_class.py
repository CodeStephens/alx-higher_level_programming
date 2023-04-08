#!/usr/bin/python3
"""
Defines a function to evaluate an object as an instance of a defined class
"""


def is_same_class(obj, a_class):
    """
    the function returns true if an object is an instance of a class
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
