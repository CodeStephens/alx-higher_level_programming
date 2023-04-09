#!/usr/bin/python3
"""
Defines a class Rectangle inheriting from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines the Rectangle class
    """
    __width = 0
    __height = 0

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
