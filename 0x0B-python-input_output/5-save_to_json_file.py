#!/usr/bin/python3
"""This is to define json file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """This is to write an object to a trxt file using JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
