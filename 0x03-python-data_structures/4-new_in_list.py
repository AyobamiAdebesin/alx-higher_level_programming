#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list[:]
    elif idx > range(len(my_list) - 1)):
        return my_list[:]
    else:
        my_list[idx] = element
        return(my_list)
