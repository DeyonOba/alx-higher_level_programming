#!/usr/bin/python3

# file_name: 2-args.py
import sys


def command_line_args():
    nargv = len(sys.argv) - 1  # argv[0] contains file name

    if nargv > 0:
        print("{:d} arguments:".format(nargv))

        for i in range(1, nargv + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
    else:
        print("{:d} arguments.".format(nargv))

if __name__ == "__main__":
    command_line_args()
