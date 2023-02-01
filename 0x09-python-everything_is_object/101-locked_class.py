#!/usr/bin/python3


class LockedClass:
    """
    prevents dynamica instantiation of instance attribute besides 'first_name'
    """

    __slots__ = ["first_name"]
