#!/usr/bin/python3
"""
This module contains a function that writes an 
object to a text file using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """A function that save to JSON"""

   with open(filename, mode='w', encoding='utf-8') as f:
       json.dump(my_obj, f)
