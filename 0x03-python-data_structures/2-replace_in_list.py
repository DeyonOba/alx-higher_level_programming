#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replace element in a list at a particular position

    Args:
        my_list (list): List containing elements
        idx (int): The index to be replaced
        element: Python permitted data structure/ type value

    Returns:
        list: A list contain elements
    """
    n = len(my_list)

    if (idx < 0) or (idx > n - 1):
        return None
    else:
        my_list[idx] = element

    return my_list


if __name__ == "__main__":
    my_list = [1, 0, 4, 2, 3]
    print("..." * 10)
    print("Test function: replace_in_list")
    print("..." * 10)
    print("List created:", my_list)
    replace_in_list(my_list, 0, 0)
    print("Re-arrange list:", my_list)
    replace_in_list(my_list, 1, 1)
    print("Re-arrange list:", my_list)
    replace_in_list(my_list, 2, 2)
    print("Re-arrange list:", my_list)
    replace_in_list(my_list, 3, 3)
    print("Re-arrange list:", my_list)
    replace_in_list(my_list, 4, 4)
    print("Re-arrange list:", my_list)
