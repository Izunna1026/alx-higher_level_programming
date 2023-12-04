#!/usr/bin/python3
def no_c(my_string):
    list_of_string = list(my_string)
    count = 0
    for string in list_of_string:
        if string == 'c' or string == 'C':
            list_of_string[count] = ""
        count += 1
    return "".join(list_of_string)
