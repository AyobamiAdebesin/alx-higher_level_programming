#!/usr/bin/python3
""" A module that add two integers together"""


def add_integer(a, b=98):
    """
    A function that adds two integers together

    Float arguments are typecasted to int before addition

    Raises:
        TypeError: If either a or b is non-integer and non-float
    """
    result = 0

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b mus be an integer")
    else:
        result = int(a) + int(b)

    return result
