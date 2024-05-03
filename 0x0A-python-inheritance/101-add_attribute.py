#!/usr/bin/python3

"""Module adds attribute to object."""


def add_attribute(obj, attr, value):
    """
    Funtion that adds attribute to object or raise error
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
