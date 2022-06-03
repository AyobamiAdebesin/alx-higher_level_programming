#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    arg_sum = 0
    for i in range(arg_len-1):
        arg_sum += int(sys.argv[i+1])
    print("{}".format(arg_sum))
