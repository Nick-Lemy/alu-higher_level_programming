#!/usr/bin/python3
def print_reversed_list_integer(my_list=[1, 2]):
    if my_list == None:
        pass
    elif len(my_list) > 0:
        for i in reversed(my_list):
            print("{:d}".format(i))
    else:
        pass
