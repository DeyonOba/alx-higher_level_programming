#!/usr/bin/python3


def no_c(my_string):
    """Remove the string c or C from a string

    Args:
        my_string (str): string containing characters

    Returns:
        String without upper or lower cas string
    """
    new_string = ""
    for c in my_string:
        if c in "cC":
            continue
        else:
            new_string += c
    return new_string


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
