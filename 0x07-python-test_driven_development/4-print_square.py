#!/usr/bin/python3
"""This is to define a square-printing function"""


def print_square(size):
    """This is to print a square with the # character

    Args:
        size (int): The height/width of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#', end="") for j in range(size)]
        print("")
