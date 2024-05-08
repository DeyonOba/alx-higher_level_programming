#!/usr/bin/python3

"""
Module writes an Object to a text file, using a JSON representation:

    - Prototype: def save_to_json_file(my_obj, filename):
    - open file using the with statement.
    - Does not manage exceptions if the object can’t be serialized.
    - Does not manage file permission exceptions.
"""
import json


def save_to_json_file(my_obj, filename) -> None:
    """Writes an Object to a text file, using Json representation."""
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
