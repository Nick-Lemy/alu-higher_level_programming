#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            i = ''
            new += i
        else:
            new += i
    return new
