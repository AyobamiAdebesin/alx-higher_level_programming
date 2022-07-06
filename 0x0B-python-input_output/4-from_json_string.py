#!/usr/bin/python3
"""This module contains a function that deserializes an object"""
import json


def from_json_string(my_str):
    """
    A function that deserializes a JSON string to a Python Object
    """
    return (json.loads(my_str))
