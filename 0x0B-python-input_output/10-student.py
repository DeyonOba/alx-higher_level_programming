#!/usr/bin/python3

"""
Write a class Student that defines a student by:

    Public instance attributes:
        - first_name
        - last_name
        - age
    - Instantiation with first_name, last_name and age:
        def __init__(self, first_name, last_name, age):
    - Public method def to_json(self, attrs=None): that retrieves a dictionary
    representation of a Student instance (same as 8-class_to_json.py):
    If attrs is a list of strings, only attribute names contained in this
    list must be retrieved. Otherwise, all attributes must be retrieved
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
        if not attrs:
            return obj_dict
        attrs_type = type(attrs[0])
        new_attrs = {
            key: value
            for key, value in obj_dict.items()
            if key in attrs and type(key) is attrs_type
            }
        return new_attrs

    def verify_attrs(self, attrs: dict = None) -> dict:
        verified_types = [list, dict, str, int, bool]
        if attrs:
            tmp = attrs.copy()
            for key, value in attrs.items():
                if type(value) not in verified_types:
                    tmp.pop(key)
            return tmp
        return {}
