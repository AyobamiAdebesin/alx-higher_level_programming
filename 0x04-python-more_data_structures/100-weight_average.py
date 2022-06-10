#!/usr/bin/python3
def weight_average(my_list=[]):
    weight_sum = 0
    weight_ave = 0
    weight_div = 0
    if len(my_list) == 0:
        return weight_ave
    for i in range(len(my_list)):
        weight_sum += my_list[i][0] * my_list[i][1]
        weight_div += my_list[i][1]
    weight_ave = weight_sum / weight_div
    return (weight_ave)
