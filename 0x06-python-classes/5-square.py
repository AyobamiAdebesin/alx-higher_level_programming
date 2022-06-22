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

    def area(self):
        """
        A method that calculates the area of the square
        """
        return (self.__size)**2

    @property
    def size(self):
        """
        A method to retrieve the private instance variable 'size'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A method to set the private instance variable 'size' to another value
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print(0)
        for i in range(self.__size):
            print("#"*self.__size, end='\n')
