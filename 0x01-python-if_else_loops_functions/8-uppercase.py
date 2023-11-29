#!/usr/bin/python3


def uppercase(string):
    for c in string:
        ascii_no = ord(c)
        if 97 <= ascii_no <= 122:
            ascii_no -= 32
        if 65 <= ascii_no <= 90:
            print("{}".format(chr(ascii_no)), end='')
        else:
            print("{}".format(chr(ascii_no)), end='')
