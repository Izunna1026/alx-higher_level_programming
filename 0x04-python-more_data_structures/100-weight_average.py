#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return (0)
    a = 0
    b = 0
    for x, y in my_list:
        a += x * y
        b += y
    return (a / b)
