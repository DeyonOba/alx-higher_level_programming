#!/usr/bin/python3

"""
Write a class Student that defines a student by: (based on 10-student.py)

    Public instance attributes:
        - first_name
        - last_name
        - age
    - Instantiation with first_name, last_name and age:
        def __init__(self, first_name, last_name, age):
    - Public method def to_json(self, attrs=None):
        that retrieves a dictionary representation of a Student
        instance (same as 8-class_to_json.py):
    - If attrs is a list of strings, only attributes name contain
    in this list must be retrieved. Otherwise, all attributes must be retrieved
    - Public method def reload_from_json(self, json):
        that replaces all attributes of the Student instance:
    - You can assume json will always be a dictionary.
    - A dictionary key will be the public attribute name.
    - A dictionary value will be the value of the public attribute.
    - You are not allowed to import any module.
"""


class Student:
    """
    Student class defines a student by first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs: list = None) -> dict:
        obj_dict = self.verify_attrs(self.__dict__)
        if attrs is None:
            return obj_dict
        if len(attrs) == 0:
            return {}
        new_attrs = {
            key: value
            for key, value in obj_dict.items()
            if key in attrs
            }
        return new_attrs

    def verify_attrs(self, attrs: dict = None,) -> dict:
        verified_types = [list, dict, str, int, bool]
        if attrs:
            tmp = attrs.copy()
            for key, value in attrs.items():
                if type(value) not in verified_types:
                    tmp.pop(key)
            return tmp
        return {}

    def reload_from_json(self, json: dict) -> None:
        for key in self.__dict__.copy():
            if key in json.keys():
                setattr(self, key, json[key])
            else:
                delattr(self, key)
