#!/usr/bin/python3


def uppercase(string):
    for c in string:
        ascii_no = ord(c)
        if 97 <= ascii_no <= 122:
            ascii_no -= 32
        print(chr(ascii_no), end='')
    print()
