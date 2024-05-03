#!/usr/bin/python3

"""Module for MyInt Class."""


class MyInt(int):
    """MyInt Class."""
    def __eq__(self, other):
        if int.__ne__(self, other):
            return True
        else:
            return False

    def __ne__(self, other):
        if int.__eq__(self, other):
            return True
        else:
            return False
