#!/usr/bin/python3
"""
This module contains a function that creates an object from
a JSON file
"""
import json


def load_from_json_file(filename):
    """A function that save to JSON"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
