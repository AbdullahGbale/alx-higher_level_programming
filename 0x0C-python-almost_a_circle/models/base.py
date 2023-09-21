#!/usr/bin/python3
"""
models/__init__.py (empty file)
models/base.py
"""
class Base:
    """Private class attribute"""
    __nb_objects = 0
    """Class constructor"""

    def __init__(self, id=None):
        """If id is provided assign it to the public instance attribute"""
        if id is not None:
            self.id = id
        else:
            """increment __nb_objects and assign the new value to the public instance attribute id"""
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
