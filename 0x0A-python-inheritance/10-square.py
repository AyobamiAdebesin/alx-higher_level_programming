#!/usr/bin/python3

"""A module that inherits from the Rectangle class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class that inherits from the Rectangle class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return ("[{}] {}/{}".
                format(type(self).__name__, self.__size, self.__size))
