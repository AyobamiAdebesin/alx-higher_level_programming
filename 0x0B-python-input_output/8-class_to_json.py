#!/usr/bin/python3
"""This module serializes a class to a JSON object"""


def class_to_json(obj):
    """ Serializes obj to JSON """
    return obj.__dict__
