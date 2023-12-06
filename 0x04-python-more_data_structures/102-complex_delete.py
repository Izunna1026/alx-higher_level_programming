#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = []
    for a, a_val in a_dictionary.items():
        if a_val is value:
            new.append(a)
    for i in new:
        del a_dictionary[i]
    return (a_dictionary)
