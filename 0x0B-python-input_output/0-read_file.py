#!/usr/bin/python3
""" This module contains a function that can read files"""


def read_file(filename=""):
    """A function that reads from file"""
    with open(filename, encoding="utf-8") as f:
        for line in f.read():
            print(line)
