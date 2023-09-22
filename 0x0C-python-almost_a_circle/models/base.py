#!/usr/bin/python3
"""Class is base"""
import json


class Base:
    """
    Represents a class Base which will act as a base class for
    other subclass
    """
    
    __nb_objects = 0 # private class attribute

    def __init__(self, id=None):
        # If id is provided assign it to the public instance attribute
        if id is not None:
            self.id = id
        else:
            # increment __nb_objects and assign the new value to the public instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returning json method representation of list dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
        return json_string
