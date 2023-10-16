#!/usr/bin/python3
"""
Module
"""
import json


class Base:
    """
    Class Doc
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Doc
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to json string doc
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save to file doc
        """
        filename = cls.__name__ + ".json"
        json_string = "[]"
        if list_objs is not None:
            json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        from json string doc
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create doc
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        lod from file doc
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_string = file.read()
                list_of_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_of_dicts]
        except FileNotFoundError:
            return []

    def update(self, *args, **kwargs):
        """
        update doc
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
