#!/usr/bin/python3
"""This is to define a python class-to-JSON function"""


def class_to_json(obj):
    """This is to return the dict representation of a simple data structure"""
    return obj.__dict__
