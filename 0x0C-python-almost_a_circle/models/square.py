#!/usr/bin/python3
"""Defines a Square class that inherits from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """String method for the square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
