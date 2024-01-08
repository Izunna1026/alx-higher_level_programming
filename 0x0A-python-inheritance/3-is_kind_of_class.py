#!/usr/bin/python3
""" This is to define a class-checking function"""


def is_kind_of_class(obj, a_class):
    """ This is checking if the object is same an instance of a given class

    Args:
        obj (any): This is the object to check
        a_class (type): the class to match the obj type
    Returns:
        if obj is same an instance of a_class - True
        Else - False
    """
    if isinstance(obj, a_class):
        return True
    return False
