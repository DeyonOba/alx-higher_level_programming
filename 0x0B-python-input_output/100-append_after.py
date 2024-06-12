#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file,
after each line containing a specific string (see example):

- Prototype: def append_after(filename="", search_string="", new_string=""):
- You must use the with statement.
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module.
"""


def append_after(filename="", search_string="", new_string="") -> None:
    """Inserts a line in text file if the search string is found."""
    with open(filename, "r+", encoding="utf-8") as file:
        text = file.readlines()
        new_lines = []
        for line in text:
            if search_string in line:
                new_lines.extend([line, new_string])
            else:
                new_lines.append(line)
        file.seek(0)
        file.writelines(new_lines)
