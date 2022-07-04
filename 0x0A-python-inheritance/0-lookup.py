#!/usr/bin/python3
"""
This module contains a function that returns the list of available
attributes and methods of an object

"""


def lookup(obj):
    """
    A function that returns the list of methods and
    attributes of an obj
    """
    return dir(obj)
