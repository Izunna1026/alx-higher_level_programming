#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        big_num = my_list[0]
        for count in range(len(my_list)):
            if my_list[count] > big_num:
                big_num = my_list[count]
        return (big_num)
