#!/usr/bin/python3
""" An empty class that defines a square"""


class Square:
    """
    An empty class that defines a square

    """
    def __init__(self, size=0, position=(0,0)):
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

        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int and type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        A function that prints a square
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for i in range(self.__size):
                    print("#", end='')
                print()
