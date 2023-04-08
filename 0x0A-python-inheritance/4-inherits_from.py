#!/usr/bin/python3
"""
Defines a function that checks the subclass identity of a given object
"""


def inherits_from(obj, a_class):
    """
    the checks if obj is an instance of a class that inherited directly or
    indirectly from a given class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
