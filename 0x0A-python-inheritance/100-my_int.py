#!/usr/bin/python3
"""This module contains a class that inherits from the int class"""


class MyInt(int):
    """
    A class that inherits from the int class, but guess what?
    ............Its a rebel...........Ahahha!!!
    """

    def __eq__(self, int2):
        return int.__ne__(self, int2)

    def __ne__(self, int2):
        return int.__eq__(self, int2)
