#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square"""
    
    def __init__(self, size=0):
        """Initializes the size of sqaure
        
        Args:
            size(int): The size of the square
            """
        self.__size = size

    @property
    def size(self):
        """Get and set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance (size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of square"""
        return (self.__size ** 2)
    
    def my_print(self):
        """prints out a square with '#' """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
