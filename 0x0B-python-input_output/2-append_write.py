#!/usr/bin/python3
"""This is to define a text file writing function"""


def append_write(filename="", text=""):
    """to write a string to the end of a UTF8 text file

    Args:
        filename (str): the name of file to write to
        text (str): the text to be written to the file
    Returns:
        the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
