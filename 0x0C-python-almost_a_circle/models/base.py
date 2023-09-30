#!/usr/bin/python3
"""Class is base"""
import json


class Base:
    """Base class for data manipulation and representation"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries into JSON string representation.

        Args:
            list_dictionaries(list): A list of dictionaries to be converted.

        Returns:
            str: A JSON string representation of the list of dictionaries.

        If list_dictionaries is None or empty, it returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save instances  to file

        Args:
            list_objs:n list of instances to be saved to JSON file.

        The filename is constructed from class name (<Class name>.json).
        If list_objs is None, it saves an empty list to the file.
        The file is overwritten if it already exists.
        """

        if list_objs is None:
            list_objs = []

            filename = cls.__name__ + ".json"

            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dictionaries)

            with open(filename, 'w') as file:
                file.write(json_string)
