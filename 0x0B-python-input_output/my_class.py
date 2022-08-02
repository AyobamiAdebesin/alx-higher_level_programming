#!/usr/bin/env python3

class MyClass:

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
         return "[MyClass] {} - {:d}".format(self.name, self.number)

if __name__ == "__main__":
    m = MyClass("John")
    class_to_json = __import__('8-class_to_json').class_to_json

    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
