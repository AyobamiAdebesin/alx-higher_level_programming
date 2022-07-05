#!/usr/bin/python3
def add_attribute(obj, name, value):
    """ Function that adds a new attribute to an object

    Args:
        obj: object
        name: attribute name
        value: attribute value

    Raises:
        TypeError: when the attribute can't be added

    """

    def add_attribute(self, attribute, value):
        """Add attribute if it's possible."""
        if hasattr(self, '__dict__'):
                setattr(self, attribute, value)
        else:
                raise TypeError("can't add new attribute")