#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        print("{}".format(value))
        return False
    else:
        return True
