#!/usr/bin/python3
"""This module contains a function that appends to a file"""


def append_write(filename="", text=""):
    """A function that writes to a file"""
    with open(filename, mode='a', encoding="utf-8") as f:
        n_chars = f.write(text)
    return n_chars
