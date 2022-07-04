#!/usr/bin/python3

"""
This module contains a function that checks if an object is an
instance of a class or if the object is an instance of a class
that inherited from the sepcified class
"""


def is_kind_of_class(obj, a_class):
    """
    A  function that checks if an object is an instance of a class
    """
    return isinstance(obj, a_class)
