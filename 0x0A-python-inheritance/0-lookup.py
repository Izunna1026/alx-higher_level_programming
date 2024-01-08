#!/usr/bin/python3

""" This is to define the job attribute of the lookup fumction"""


def lookup(obj):
    """ To return the list of object's available attributes."""
    return (dir(obj))
