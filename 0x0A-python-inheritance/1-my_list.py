#!/usr/bin/python3

"""To define list class that was inherited"""


class MyList(list):
    """To implement the sorted printing for the built-in list class"""

    def print_sorted(self):
        """This is to print a list in ascending sorted order"""
        print(sorted(self))
