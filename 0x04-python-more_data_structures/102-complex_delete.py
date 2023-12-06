#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete key with a specific value"""
    new_dict = {}

    for key in a_dictionary:
        if a_dictionary[key] != value:
            new_dict.update({key: a_dictionary[key]})
    return new_dict


if __name__ == "__main__":
    my_dict = {"black": "white", "up": "down"}
    print("New dictionary without key (up)")
    print(complex_delete(my_dict, "down"))
