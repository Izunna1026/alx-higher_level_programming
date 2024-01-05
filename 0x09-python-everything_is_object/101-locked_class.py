#!/usr/bin/python3
"""This is to define locked class"""


class LockedClass:
    """
    This is to prevent any user instantiating a lockedclass attributes
    but called first_name
    """

    __slots__ = ["first_name"]
