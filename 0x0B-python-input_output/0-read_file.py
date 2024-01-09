#!/usr/bin/python3
"""This is to define a text file reading function"""


def read_file(filename=""):
    """to print the contant of UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
