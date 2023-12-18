#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    inp = 0
    for val in range(x):
        try:
            print("{}".format(my_list[val]), end="")
            inp += 1
        except IndexError:
            break
    print("")
    return (inp)
