#!/usr/bin/python3
def print_sorted_dictionary(my_dictionary):
    for keys in sorted(my_dictionary.keys()):
        print('{}: {}'.format(keys, my_dictionary[keys]))
