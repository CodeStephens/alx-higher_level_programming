#!/usr/bin/python3
"""
Defines a function to evaluate an object as an instance of a defined class
"""


def is_kind_of_class(obj, a_class):
    """
    the function returns true if an object is an instance of a class/dub-class
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
