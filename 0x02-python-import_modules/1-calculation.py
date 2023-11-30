#!/usr/bin/python3

# file name: 1-calculation.py
import calculator_1

if __name__ == "__main__":
    # Declare and assign variables a and b
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, calculator_1.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, calculator_1.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, calculator_1.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, calculator_1.div(a, b)))
