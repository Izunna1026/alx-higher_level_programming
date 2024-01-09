#!/usr/bin/python3
"""this si to define a text file to insert in a function"""


def append_after(filename="", search_string="", new_string=""):
    """to input text after each line that has a given string in a file

    Args:
        filename (str): the name of the file
        search_string (str): the string to search within the file
        new_string (str): the string to be added
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
