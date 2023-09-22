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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Implementing class method to write
        to a file
        """
        if list_objs is None or len(list_objs) == 0:
            json_string = "[]"
        else:
            filename = cls.__name__ + ".json"

            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dictionaries)

        with open(filename, 'w') as file:
            file.write(json_string)

