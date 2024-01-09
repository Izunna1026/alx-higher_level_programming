#!/usr/bin/python3
"""This is to define JSON file reading function"""
import json


def load_from_json_file(filename):
    """to create a python object from json file"""
    with open(filename) as f:
        return json.load(f)
