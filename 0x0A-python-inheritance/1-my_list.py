#!/usr/bin/python3

"""A module that contains a class that inherits from a List class"""


class MyList(list):
    """
    A class that inherits from a base class and prints
    the elements of a list in a sorted manner

    """

    def __init__(self):
        pass

    def print_sorted(self):
        return(self.sort())
