#!/usr/bin/python3
"""This is to define a name printing function"""


def say_my_name(first_name, last_name=""):
    """this is to print a name


    Args:
        first_name (str): the first name to print
        last_name (str): the last name
    Raises:
        TypeError: if any os the names is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
