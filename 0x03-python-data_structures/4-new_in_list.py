#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Replace element in a list at a particular position

    Args:
        my_list (list): List containing elements
        idx (int): The index to be replaced
        element: Python permitted data structure/ type value

    Returns:
        list: A list contain elements
    """
    new_list = my_list.copy()
    n = len(new_list)

    if (idx < 0) or (idx > n - 1):
        return new_list
    else:
        new_list[idx] = element

    return new_list


if __name__ == "__main__":
    my_list = [1, 0, 4, 2, 3]
    print("..." * 10)
    print("Test function: new_in_list")
    print("..." * 10)
    new_list = new_in_list(my_list, 0, 0)

    print("Original list:", my_list)
    print("New list:", new_list)
