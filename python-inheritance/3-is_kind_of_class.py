#!/usr/bin/pytohn3

"""
modulo que contiene la clase(?
"""


def is_kind_of_class(obj, a_class):
    """
    True if the object is an instance of, or if the object
    is an instance of a class that inherited from
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
