#!/usr/bin/python3

"""
module documented task 9
"""


class Student:
    """
    class documented task 9
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key) for
                    key in attrs if hasattr(self, key)}
