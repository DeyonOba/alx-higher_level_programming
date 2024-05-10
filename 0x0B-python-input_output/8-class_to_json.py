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
to_json_string = __import__("3-to_json_string").to_json_string


def class_to_json(obj):
    """
    Dictionary description of a basic data structure.
    """
    obj_attr = obj.__dict__
    return to_json_string(obj_attr)
