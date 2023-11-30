#!/usr/bin/python3

import sys

def add_argv():
    total = 0
    nargs = len(sys.argv)

    for i in range(1, nargs):
        total += int(sys.argv[i])
    print("{:d}".format(total))

if __name__ == "__main__":
    add_argv()
