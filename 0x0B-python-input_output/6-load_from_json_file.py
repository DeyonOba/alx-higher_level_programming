#!/usr/bin/python3

"""
Module returns the JSON representation of an object (string):

- Prototype: load_from_json_file(filename):
- Use with statement to open.
- Does not manage exceptions if the object can’t be serialized.
- Does not manage file permissions / exceptions.
"""
import json


def load_from_json_file(filename: str) -> None:
    """Displays the JSON representation of an object."""
    with open(filename, encoding="utf-8") as file:
        obj = json.load(file)
        return obj
