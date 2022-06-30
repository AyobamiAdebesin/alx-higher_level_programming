#!/usr/bin/python3
""" A class that defines a Recatngle"""


class Rectangle:
    """A class that defines a Rectangle"""

    number_of_instances = 0
    print_symbol = "3"

    def __init__(self, width=0, height=0):
        """ A method that initializes the instance attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """A getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.height + self.width))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            hash_width = "{}".format(self.print_symbol) * self.__width
            return '\n'.join((hash_width) for height in range(self.__height))

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
