#!/usr/bin/python3
""" An empty class that defines a square"""


class Square:
    """
    An empty class that defines a square

    """
    def __init__(self, size=0):
        """
        Initializes the instance attributes of the class

        Args:
            self (None): The initialization parameter
        Return:
            None

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
