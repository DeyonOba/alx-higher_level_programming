#!/usr/bin/python3
def uniq_add(my_list=[]):
    max_num = 0
    sum_ = 0
    n = len(my_list)

    for i in range(n):
        if i == 0:
            max_num = my_list[i]
            sum_ = my_list[i]
        elif my_list[i] > max_num:
            max_num = my_list[i]
            sum_ += my_list[i]
        else:
            continue

    return sum_


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
