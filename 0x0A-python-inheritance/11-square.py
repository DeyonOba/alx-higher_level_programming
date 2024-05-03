#!/usr/bin/python3

"""Module for Square Class.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self._size = size

    def __str__(self):
        return "[Square] {}/{}".format(self._size, self._size)
