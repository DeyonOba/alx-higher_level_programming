#!/usr/bin/python3
"""Square"""


class Square:
    """Class that defines a square size.

    Attributes:
        size (int, float): size of a square
    """
    def __init__(self, size):
        """Object initialization.

        Args:
            size: size of square
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
