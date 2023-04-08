#!/usr/bin/python3 
"""
Defines the lookup method/function with the object attribute
"""


def lookup(obj):
    """
    lookup method returns a list of all attributes and methods
    """
    return (dir(obj))
