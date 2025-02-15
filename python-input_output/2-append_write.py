#!/usr/bin/python3

"""
module defined task 2
"""


def append_write(filename="", text=""):
    """
    function defined task 2
    """
    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)
