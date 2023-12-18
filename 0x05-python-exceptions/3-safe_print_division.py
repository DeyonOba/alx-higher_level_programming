#!/usr/bin/python3
def safe_print_division(a, b):
    divide = 0
    try:
        divide = a / b
    except ZeroDivisionError:
        divide = None
    finally:
        print("Inside result: {}".format(divide))
        return divide


if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
