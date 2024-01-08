#!/usr/bin/python3
"""This is define the class MyInt that inherits from int"""


class MyInt(int):
    """ This is to invert int operators == and !="""

    def __eq__(self, value):
        """overide == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """overide != operator with == behavior"""
        return self.real == value
