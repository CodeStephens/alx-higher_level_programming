#!/usr/bin/python3
"""
Defines a class BaseGeometry with 2 public instance method
"""


class BaseGeometry():
    """
    This is an empty class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method validates the data value as a positive integer
        """
        self.value = value
        if !(isinstance(self.value, int)):
            raise TypeError(f"{name} must be an integer")
        if self.value <= 0:
            raise ValueError(f"{name" must be greater than 0")
