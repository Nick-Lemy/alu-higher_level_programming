#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        result =[]
        for i in my_list:
            if my_list[i] != my_list[idx]:
                result.append(i)
            else:
                pass
        my_list = result
        return my_list
