#!/usr/bin/env python3
"""This module serializes a class to a JSON object"""


def class_to_json(obj):
    """ Serializes obj to JSON """
    my_dict = {}
    for key, value in (obj.__dict__).items():
        my_dict[key] = value
    return my_dict
