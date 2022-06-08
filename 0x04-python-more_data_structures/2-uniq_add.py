#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq_list = []
    for i in range(len(my_list)):
        if my_list[i] not in uniq_list:
            uniq_list.append(my_list[i])
            sum += my_list[i]
    return sum
