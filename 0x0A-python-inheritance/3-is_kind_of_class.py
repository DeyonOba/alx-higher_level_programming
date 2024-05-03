#!/usr/bin/python3

"""
Module asserts if an object is an instance of the specified class or sub.
"""


def is_kind_of_class(obj, a_class) -> bool:
    """
    Confirms if an object is an exactly instance of a class or subclass.

    Args:
    obj: An object
    a_class: Specified class

    Returns:
    bool
    """
    return isinstance(obj, a_class)
