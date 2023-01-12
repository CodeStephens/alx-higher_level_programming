#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    average = 0
    size = 0
    for item in my_list:
        average += (item[0] * item[1])
        size += item[1]
    return (average / size)
