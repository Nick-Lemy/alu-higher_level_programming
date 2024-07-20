#!/usr/bin/python3
"""
Student to JSON with filter
"""


class Student:
    """
    Student Class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
         if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                result = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        result[attr] = getattr(self, attr)
                return result

        return self.__dict__

