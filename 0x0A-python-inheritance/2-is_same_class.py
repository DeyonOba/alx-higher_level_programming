#!/usr/bin/python3

"""
Module asserts if an object is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class) -> bool:
    """Confirms if an object is an exactly instance of a class.

    Args:
    obj: An object
    a_class: Specified class

    Returns:
    bool
    """
    return type(obj) is a_class
