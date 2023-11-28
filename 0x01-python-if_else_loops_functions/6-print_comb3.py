#!/usr/bin/python3

for number in range(0, 100):
    if number == 99:
        print("{:d}".format(number))
    elif 1 != number != 10:
        print("{:02d}".format(number), end=", ")
