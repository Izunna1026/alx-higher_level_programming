#!/usr/bin/python3

"""To define class square"""


class Square:
    """To represent a square"""

    def __init__(self, size=0):
        """Initializing a new square

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
