#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary.keys():
        pass
    else:
        del a_dictionary[key]
    return (a_dictionary)
