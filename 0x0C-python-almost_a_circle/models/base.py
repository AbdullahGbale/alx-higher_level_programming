#!/usr/bin/python3
"""Class is base"""
import json


class Base:
    """
    Represents a class Base which will act as a base class for
    other subclass
    """
    
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Implementing the json method"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
        return json_string
