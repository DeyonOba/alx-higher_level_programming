#!/usr/bin/python3


def element_at(my_list, idx):
    """
    Get element at a particular index.

    Args:
        my_list: list
            List containing elements
        idx: int
            Index of the list

    Returns:
        Element in the list
    """
    n = len(my_list)

    if (idx < 0) or (idx > n - 1):
        return None
    else:
        return my_list[idx]


if __name__ == "__main__":
    my_list = [23, -90, 12, 0, 7]

    print("..." * 10)
    print("Test function: element_at")
    print("..." * 10)
    print("Test List:", my_list)
    print("Element at index {:d} is {}".format(0, element_at(my_list, 0)))
    print("Element at index {:d} is {}".format(100, element_at(my_list, 100)))
    print("Element at index {:d} is {}".format(4, element_at(my_list, 4)))
    print("Element at index {:d} is {}".format(-1, element_at(my_list, -1)))
    print("Element at index {:d} is {}".format(1, element_at(my_list, 1)))
