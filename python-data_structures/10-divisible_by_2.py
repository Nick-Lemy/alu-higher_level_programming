#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    if len(my_list) > 0:
        for i in my_list:
            if i % 2 == 0:
                result.append(True)
            else:
                result.append(False)
    return result
