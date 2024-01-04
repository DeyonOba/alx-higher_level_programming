#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class.

    Attribute:
        width (int): The width measurement
        height (int): Integer measurement greater than 0
    """
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        else:
            output = []
            for i in range(self.height):
                output.append("#"*self.width)
            return "\n".join(output)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


if __name__ == "__main__":
    my_rectangle_1 = Rectangle(2, 4)
    my_rectangle_2 = Rectangle(2, 4)
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_1
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_2
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
