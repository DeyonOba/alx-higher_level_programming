#!/usr/bin/python3

"""Module lists the available attributes and methods of an object."""


def lookup(obj):
    """
    List of available attributes and methods of an object.

    Parameters
    - obj: Class object

    Returns
    - list
    """
    return dir(obj)


if __name__ == "__main__":

    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
