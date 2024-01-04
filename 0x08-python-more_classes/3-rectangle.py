#!/usr/bin/python3
"""This is to define a rectangle class"""


class Rectangle:
    """ This is to to represent a class name rectangle"""

    def __init__(self, width=0, height=0):
        """this is initializing a new rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """this is to get the width of the rectangle"""
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
        """this is to get the height of thr rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This is to get the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """This is to return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """this is to return the printable rep of the rectangle

        and to represent the rectangle wih # character
        """
        if self.__width == 0 or self.height == 0:
            return ("")

        size = []
        for k in range(self.__height):
            [size.append('#') for f in range(self.__width)]
            if k != self.__height - 1:
                size.append("\n")
        return ("".join(rect))
