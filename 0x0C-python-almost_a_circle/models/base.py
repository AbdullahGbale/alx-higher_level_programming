#!/usr/bin/python3
"""Class is base"""
import json


class Base:
    """Base class for data manipulation and represenation"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries into JSON string representation.
        
        Args:
            list_dictionaries(list): A list of dictionaries to be converted.

        Returns:
            str: A JSON string representation of the list of dictionaries.

        If list_dictionaries is None or empty, it returns "[]".
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
        return json_string

     @classmethod
    def save_to_file(cls, list_objs):
        """
        Implementing the class methodto write the string
        representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)

        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the string of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Defines class method that returns a list of instances"""
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        dict_list = cls.from_json_string(json_string)
        instances = [
                cls.create(**dictionary)
                for dictionary in dict_list
            ]
        return instances
