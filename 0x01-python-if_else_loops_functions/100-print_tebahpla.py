#!/usr/bin/python3

for ascii_no in range(122, 96, -1):
    if ascii_no % 2 != 0:
        ascii_no -= 32
    print(chr(ascii_no), end="")
