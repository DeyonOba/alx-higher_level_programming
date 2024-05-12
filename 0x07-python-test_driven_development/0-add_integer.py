#!/usr/bin/python3

"""
Module contains function that adds 2 integers:

    - Prototype: def add_integer(a, b=98)
    - `a` and `b` must be integers or floats, otherwise raise a TypeError
        exception with the message "a must be an integer" or
        "b must be an integer.
    - `a` and `b` must be first casted to integers if they are float.
    - Returns an integer: the addition of `a` and `b`.
    - No library dependencies is needed in this module.
"""


def add_integer(a, b=98):
    """Adds to integers together."""
    valid_types = [int, float]

    if type(a) not in valid_types:
        raise TypeError("a must be an integer")
    if type(b) not in valid_types:
        raise TypeError("b must be an integer")

    addition = int(a) + int(b)
    return addition


if __name__ == "__main__":
    print(add_integer(1))
