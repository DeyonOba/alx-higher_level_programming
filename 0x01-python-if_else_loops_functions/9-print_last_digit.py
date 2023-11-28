#!/usr/bin/python3


def digit_count(number):
    """Get the number of digits in a given number"""
    count = 0
    while True:
        number = number // 10  # Count down by 10
        count += 1  # Increment count
        if number == 0:
            return count


def get_last_digit(number):
    """Get the last digit of a number"""

    #  Assign variable is_negative to check for negative values
    is_negative = True

    if number == 0:
        return number
    elif number > 0:  # When number is positive is_negative is false
        is_negative = False
    else:
        number = -1 * number  # Convert negative number to positive

    count = digit_count(number) - 1  # Assign only the unit portion
    for power in range(count, 0, -1):  # Count down from digit count
        int_div = number // (10 ** power)
        number = number - (int_div * 10**power)

    return number


def print_last_digit(number):
    last_digit = get_last_digit(number)
    print(last_digit, end='')
    return last_digit
