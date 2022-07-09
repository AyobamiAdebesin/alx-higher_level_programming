#!/usr/bin/python3
""" 
This module contains a script that adds all arguments
to a Python lis and then save them to a file
"""
import os
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_josn_file = __import__("6-load_from_json_file").load_from_json_file

my_list = []
filename = "add_item.json"

if os.path.exists(
