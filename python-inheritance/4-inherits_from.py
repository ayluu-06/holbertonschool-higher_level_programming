#!/usr/bin/python3

"""
modulo que contiene la clase(?
"""


def inherits_from(obj, a_class):
    """
    if the object is an instance of a class that inherited
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
