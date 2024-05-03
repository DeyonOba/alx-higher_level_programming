#!/usr/bin/python3

"""Module contain MyList that inherits from the list class."""


class MyList(list):
    """MyList inherits attributes from list.

    MyList has a method `print_sorted` that sorts list in ascending order
    """
    def __init__(self) -> None:
        """Initialize the class MyList"""
        super().__init__()

    def print_sorted(self):
        """Display sorted new list in ascending order"""
        print(sorted(self))
