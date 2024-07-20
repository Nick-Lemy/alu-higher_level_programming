#!/usr/bin/python3
"""
Write file in python
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8) and returns the number of characters written
    """

    a=0
    with open(filename, 'w') as f:
        f.write(f'{text}')
        for i in text:
            a+=1
        return a