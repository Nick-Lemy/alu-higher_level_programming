#!/usr/bin/python3

"""
Append Write
"""


def append_write(filename="", text=""):
    """
    Function that returns the number of characters added after happened them
    """
    a = 0
    with open(filename, 'a') as f:
        f.write(text)
        for i in text:
            a += 1
        return a
