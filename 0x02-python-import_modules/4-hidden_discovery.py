#!/usr/bin/python3
import hidden_4
for name in dir(hidden_4):
    if name[0] != '_' and name[1] != '_':
        print(name)
