#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    new_dict.values = list(map(lambda x: x * 2, a_dictionary.values))
    return new_dict
