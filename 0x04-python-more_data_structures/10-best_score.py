#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    dict_keys = list(a_dictionary.key())
    max_key = ""
    max_score = a_dictionary[dict_keys[0]]
    for key in dict_keys:
        if a_dictionary[key] > max_score:
            max_score = a_dictionary[key]
            max_key = key
    return max_key
