#!/usr/bin/python3

"""
This module contains a function that checks if an object is an
instance of a class
"""


def is_same_class(obj, a_class):
    """
    A  function that checks if an object is an instance of a class
    """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False
