#!/usr/bin/python3

"""
This module contains a function that checks if an object is an
instance of a class or if the object is an instance of a class
that inherited from the sepcified class
"""


def inherits_from(obj, a_class):
    """
    A  function that checks if an object is an instance of a class
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
