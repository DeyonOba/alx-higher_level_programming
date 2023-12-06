#!/usr/bin/python3


def weight_average(my_list=[]):
    """Get the Weight Average of a list"""
    total = 0
    n = 0
    
    if len(my_list) == 0:
        return 0

    for i in my_list:
        total += i[0] * i[1]
        n += i[1]
    return (total / n)


if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
