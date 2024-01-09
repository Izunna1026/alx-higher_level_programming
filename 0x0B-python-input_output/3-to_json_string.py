#!/usr/bin/python3
"""This is to define a string to JSON function"""
import json


def to_json_string(my_obj):
    """This is to return JSON representation of a sting"""
    return json.dumps(my_obj)
