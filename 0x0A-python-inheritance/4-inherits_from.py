#!/usr/bin/python3

"""
Module asserts if an object is subclass of the specified class.
"""


def inherits_from(obj, a_class) -> bool:
    """
    Confirms if an object is a subclass of a specified class.

    Args:
    obj: An object
    a_class: Specified class

    Returns:
    bool
    """
    return issubclass(type(obj), a_class)
