#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        print("", end="")
    else:
        my_list.reverse()
        for count in my_list:
            print("{:d}".format(count))
