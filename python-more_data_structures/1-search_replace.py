#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in mylist:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
