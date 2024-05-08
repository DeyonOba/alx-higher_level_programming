#!/usr/bin/python3

"""
Module returns an object (Python data structure) represented
by a JSON string:

- Prototype: def from_json_string(my_str):
- You don’t need to manage exceptions if the object can’t be serialized.
"""
import json
import io


def from_json_string(my_str) -> str:
    """Displays the JSON representation of an object."""
    return json.load(io.StringIO(my_str))
