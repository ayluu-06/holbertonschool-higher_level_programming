#!/usr/bin/python3

"""
class that defines a square
"""


class Square:
    """
    space to start defining the square
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
    pass
