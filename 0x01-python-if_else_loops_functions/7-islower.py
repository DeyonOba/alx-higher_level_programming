#!/usr/bin/python3


def islower(char):
    ascii_no = ord(char)
    if 97 <= ascii_no <= 122:
        return True
    else:
        return False
