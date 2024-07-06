#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    b = 0
    for i in my_list:
        b+=1
    a = 0
    try:
        for i in range(0, x):
            print(my_list[i], end="" if i < b - 1 else "\n")
            a += 1
    except :
        return a
    finally:
        return a
