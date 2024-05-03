#!/usr/bin/python3

"""Class (BaseGeometry)."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits from BaseGeometry."""
    def __init__(self, width: int, height: int) -> None:
        super().integer_validator("width", width)
        self._width = width
        super().integer_validator("height", height)
        self._height = height
