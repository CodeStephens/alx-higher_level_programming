#!/usr/bin/python3


class LockedClass:
    """ dynamically prohibits the creation of instance attribute without
    reference to 'first_name'
    """
    __slots__ = ['first_name']
    def __init__(self, first_name):
        self.first_name = first_name
