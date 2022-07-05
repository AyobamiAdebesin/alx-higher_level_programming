#!/usr/bin/python3
"""This module contains a class that inherits from the int class"""


class MyInt(int):
    """
    A class that inherits from the int class, but guess what?
    ............Its a rebel...........Ahahha!!!
    """

    def __eq__(int1, int2):
        if int1 == int2:
            return False

    def __neq__(int1, int2):
        if int1 != int2:
            return True
