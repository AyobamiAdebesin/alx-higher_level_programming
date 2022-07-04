#!/usr/bin/python3

def tail(filename, n=10):
    with open(filename, "r") as f:
        lines = f.readlines()
        print(type(lines))
    for line in lines[len(lines)-n:]:
        print(line)

if __name__ == "__main__":
    filename = "hello.txt"

    tail(filename, 10)
