#!/usr/bin/python3

"""
Module returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization
of an object:

    - Prototype: def class_to_json(obj):
    - obj is an instance of a Class
    - All attributes of the obj Class are serializable:
        list, dictionary, string, integer and boolean
    - You are not allowed to import any module
"""


def class_to_json(obj):
    """
    Dictionary description of a basic data structure.
    """
    verified_types = [list, dict, str, int, bool]
    obj_attr = obj.__dict__
    for key, value in obj_attr.copy().items():
        if type(value) not in verified_types:
            obj_attr.pop(key)
    return obj_attr
