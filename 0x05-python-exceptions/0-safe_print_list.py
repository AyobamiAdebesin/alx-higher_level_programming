#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except IndexError:
            break
        else:
            element_count += 1
    print()
    return (element_count)
