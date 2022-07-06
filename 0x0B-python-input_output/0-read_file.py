#!/usr/bin/python3
""" This module contains a function that can read files"""


def read_file(filename=""):
    """A function that reads from file"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read()
