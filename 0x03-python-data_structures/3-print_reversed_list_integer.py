#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    Print all integer values in reverse order

    Args:
        my_list (list): Contains list of integer

    Returns:
        Element of list in reversed order, 1 element per line
    """
    n = len(my_list)

    # The list method reverse can also be used here
    for i in range(n - 1, -1, -1):
        print("{:d}".format(my_list[i]))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    print_reversed_list_integer(my_list)
