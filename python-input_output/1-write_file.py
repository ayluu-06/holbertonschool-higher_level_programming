#!/usr/bin/python3

"""
module decumented task 1
"""


def read_file(filename=""):
    """
    function documented task 0
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")


def write_file(filename="", text=""):
    """
    function documented task 1
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
