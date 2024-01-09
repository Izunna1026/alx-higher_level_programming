#!/usr/bin/python3
# 6-from_json_string.py
"""This sis to define a json-to-object function"""
import json


def from_json_string(my_str):
    """this is returning the python object of json string"""
    return json.loads(my_str)
