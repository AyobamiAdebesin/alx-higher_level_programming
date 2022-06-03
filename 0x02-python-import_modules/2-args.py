#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    if arg_len == 1:
        print("{} arguments.".format(arg_len-1))
    elif arg_len == 2:
        print("{} argument:".format(arg_len-1))
        print("{}: {}".format(arg_len-1, sys.argv[arg_len-1]))
    else:
        print("{} arguments:".format(arg_len-1))
        for i in range(arg_len-1):
            print("{}: ".format(i+1), end='')
            print(sys.argv[i+1])
