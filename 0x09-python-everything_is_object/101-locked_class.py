#!/usr/bin/python3
""" Defines a locked class """

class LockedClass:
    """
    prevents dynamica instantiation of instance attribute besides 'first_name'
    """

    __slots__ = ["first_name"]
