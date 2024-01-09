#!/usr/bin/python3
"""This is to define a text file writing function"""


def write_file(filename="", text=""):
    """to write a string to a UTF8 text file

    Args:
        filename (str): the name of file
        text (str): the text to be written to the file
    Returns:
        the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
