#!/usr/bin/python3

"""
This module appends a text to a text file (UTF8) and returns the number of
character written:

    - Prototype: def append_write(filename="", text=""):
    - Write to file using the with statement
    - File permission or file doesn't exist exceptions are ignored.
    - Creates the file if the file does not exist.
    - Does not over-write an already existing file.
    - No dependencies are needed.
"""


def append_write(filename="", text="") -> int:
    """
    Writes to a text file that exists.

    Parameters
    ----------
    filename : str
        Combination of file path, file name, and file extension.
    text : str
        Text to be added to text file.

    Returns
    -------
    char_count : int
        The number of character written to text file
    """
    char_count = 0

    with open(filename, mode="a", encoding="utf-8") as file:
        char_count += file.write(text)

    return(char_count)
