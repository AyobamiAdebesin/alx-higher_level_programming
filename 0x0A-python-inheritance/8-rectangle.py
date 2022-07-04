#!/usr/bin/python3
"""
This module contains a class that inherits from a super class

"""
from 7-base-geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits from a super class

    """

    def __init__(self, width, height):
        self.integer_validator(name="width", value=width)
        self.integer_validator(name="height", value=height)
        self.__height = height
        self.__width = width
