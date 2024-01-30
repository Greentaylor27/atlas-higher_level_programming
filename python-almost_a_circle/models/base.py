#!/usr/bin/python3
"""
Empty base class
"""
import json


class Base:
    """
    Parent class for an almost circle
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
        """
        Method that returns the JSON representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that writes the JSON representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        json_str = cls.to_json_string(list_dicts)
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(json_str)
