#!/usr/bin/python3

"""Class (BaseGeometry)."""


class BaseGeometry:
    """New Class."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class inherits from BaseGeometry."""
    def __init__(self, width: int, height: int) -> None:
        super().__init__()

        if width is not int or width <= 0:
            self.integer_validator("width", width)
        else:
            self._width = width
        if height is not int or height <= 0:
            self.integer_validator("height", height)
        else:
            self._height = height
