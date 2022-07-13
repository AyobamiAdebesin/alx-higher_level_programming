#!/usr/bin/python3
""" This module defines a base model class"""


class Base:
    """ A Base model class

    Base: Represents the "base" for all other classes

    Attributes:
        __nb_objects(int): The number of instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a new Base class.

        Args:
            id (int): The identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
