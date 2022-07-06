#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def write_file(filename="", mode='w', text=""):
    """A function that writes to a file"""
    with open(filename, encoding="utf-8") as f:
        n_chars = f.write(text)
    return n_chars

