#!/usr/bin/python3
"""This is to define the function that adds attributed to objects"""


def add_attribute(obj, att, value):
    """ This is to add new attribute to an object if possible

    Args:
        obj (any): The object to be added to an attribute
        att (str): the attribute nsme to be added to obj
        Value (any): The value of the att
    Raises:
        TypeError: If the atribute cnnot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
