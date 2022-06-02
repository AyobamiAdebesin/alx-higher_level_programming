#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
out_str = "and is less than"
out_str1 = "Last digit of"
if number < 0:
    last = number % -10
    if last == 0:
        print(f"{out_str} {number:d} is {0} and is {0}")
    else:
        print(f"{out_str1} {number:d} is {last:d} {out_str} {6} and not {0}")
elif number >= 0:
    last = number % 10
    if last > 5:
        print(f"{out_str1} {number:d} is {last:d} and is greater than 5")
    elif last == 0:
        print(f"{out_str1} {number:d} is {0} and is {0}")
