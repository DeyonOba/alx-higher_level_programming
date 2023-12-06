#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_ = 0
    new_set = set(my_list)

    for item in new_set:
        sum_ += item
    return sum_


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
