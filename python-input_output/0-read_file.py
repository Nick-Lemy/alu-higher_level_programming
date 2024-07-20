#!/usr/bin/python3

"""
Simple Python file with a fuction that open files
"""

def read_file(filename = ""):
    """
    Function That opens files with UTF8 encoding
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end = "")