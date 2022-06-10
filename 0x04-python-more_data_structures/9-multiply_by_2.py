#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    dict_keys = list(a_dictionary.keys())
    for key in dict_keys:
        new_dict[key] *= 2
    return new_dict
