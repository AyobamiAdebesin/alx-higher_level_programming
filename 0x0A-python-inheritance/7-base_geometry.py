#!/usr/bin/python3
"""
This module contains the empty BaseGeometry class
"""


class BaseGeometry:
    """ A class the defines a geometry object"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
