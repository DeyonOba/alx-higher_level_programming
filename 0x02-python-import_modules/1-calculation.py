#!/usr/bin/python3

# file name: 1-calculation.py
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Declare and assign variables a and b
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
