#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class.

    Attribute:
        width (int): The width measurement
    """
    @staticmethod
    def check_value(value, var_name):
        if not isinstance(value, int):
            raise TypeError(f"{var_name} must be an integer")
        if value < 0:
            raise ValueError(f"{var_name} must be >= 0")

    def __init__(self, width=0, height=0):
        Rectangle.check_value(width, "width")
        Rectangle.check_value(height, "height")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the attribute width"""
        return self.__width

    @property
    def height(self):
        """Get the attribute height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the attribute width"""
        Rectangle.check_value(value, "width")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value of the attribute height"""
        Rectangle.check_value(value, "height")
        self.__height = value


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
