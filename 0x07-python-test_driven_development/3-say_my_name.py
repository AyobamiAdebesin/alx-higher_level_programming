#!/usr/bin/python3
"""
This module contains a function that prints a name
"""

def say_my_name(first_name, last_name=""):
        """
        
        A function that prints a name in full

        Args:
                first_name: The first name (string)
                last_name: The last name(string)
        
        Return:
                None

        Raises:
                TypeError: if first name is not a string
                TypeError: if last_name is not a string

        """

        if type(first_name) is not str:
                raise TypeError("first_name must be a string")

        if type(last_name) is not str:
                raise TypeError("last_name must be a string")
        
        print("My name is {} {}".format(first_name, last_name))
