#!/usr/bin/python3
def max_integer(my_list):
    if len(my_list) == 0:
        return None
    else:
       return  sorted(my_list)[-1]
print(max_integer([1, 90, 2, 13, 34, 5, -13, 3]))
