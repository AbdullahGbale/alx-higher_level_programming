#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square is the class"""

    def __init__(self, size=0):
        """Initializes size to zero

        Args:
            size: can not be less than zero"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
