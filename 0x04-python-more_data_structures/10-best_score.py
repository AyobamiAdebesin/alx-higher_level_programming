#!/usr/bin/python3
def best_score(a_dictonary):
    if not a_dictionary:
        return None
    dict_keys = list(a_dictionary.keys())
    max_score = a_dictionary[dict_keys[0]]
    max_key = ""
    for key in dict_keys:
        if a_dictionary[key] > max_score:
            max_score = a_dictionary[key]
            max_key = key
    return max_key
