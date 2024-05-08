#!/usr/bin/python3

"""
Module adds all command line arguments to a Python list,
and then save them to a file:

    - Function uses save_to_json_file from 5-save_to_json_file.py
    - Function uses load_from_json_file from 6-load_from_json_file.py
    - The list is saved as a JSON representation in a file named add_item.json
    - If the file doesn’t exist, it should be created
    - Does not manage file permissions / exceptions.
"""
import json
import sys
# import global functions `save_to_json_file` and `load_from_json_file`
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def main(args: list) -> None:
    """
    Adds all command line arguments to a python list, and saves file.

    If no command argument is been passed then an empty list passed as
    args, and then saved

    Parameters
    ----------
    args : list
        List of command line arguments.

    Returns
    -------
    None
    """
    filename = "add_item.json"

    try:
        list_obj = load_from_json_file(filename)
        list_obj.extend(args)
        save_to_json_file(list_obj, filename)
    except Exception:
        save_to_json_file(args, filename)


if __name__ == "__main__":
    args = sys.argv[1:]  # Remove the module name from argv

    main(args)
