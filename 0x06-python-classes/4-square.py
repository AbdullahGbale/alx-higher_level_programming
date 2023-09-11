#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square is the class"""

    def __init__(self, size=0):
        """Initializes size to zero

        Args:
            size(int): can not be less than zero
            """
    
    @property
    def size(self, value):
        """Retrieves value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of square"""
        return self.__size ** 2
