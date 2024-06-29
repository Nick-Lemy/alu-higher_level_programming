#!/usr/bin/python3
def print_reversed_list_integer(my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
    my_list.reverse()
    for i in my_list:
        print("{}".format(i))
