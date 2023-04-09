#!/usr/bin/python3
"""
Defines a class Rectangle inheriting from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines the Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        instantiation of the Rectangle class
        """
        self.__width = width
        self.__height = height
        integer_validator("width", width)
        integer_validator("height", height)
