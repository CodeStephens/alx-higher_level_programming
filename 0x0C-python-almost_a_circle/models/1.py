#!/usr/bin/python3 
""" defining the Base class required for the 'almost a circle' project """


class Base:
    """defining private class attribute and instance attributes """
    __nb_objects = 0

    def __init__(self, id=None):
    """ initialiazing the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
