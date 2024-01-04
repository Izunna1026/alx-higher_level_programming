#!/usr/bin/python3
"""this is to define a rectangle class"""


class Rectangle:
    """ this is to represent the class name rectangle"""

    def __init__(self, width=0, height=0):
        """this is to initialize a new rectangle


        Args:
            width (int): This is the width of the new rectangle
            height (int): this is the height of the new rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """To get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To get tge height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
