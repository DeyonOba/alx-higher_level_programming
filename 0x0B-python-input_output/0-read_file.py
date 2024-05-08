#!/usr/bin/python3

"""
This module reads a text file (UTF8) and prints it to stdout:

    - Prototype: def read_file(filename=""):
    - Reads file using the with statement
    - File permission or file doesn't exist exceptions are ignored.
    - No dependencies are needed.
"""


def read_file(filename="") -> None:
    """Read a file and display the content.

    Parameters
    ----------
    filename : str
        Contains the path and the filename with it's file extension
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
