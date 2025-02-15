#!/usr/bin/python3
"""
module decumented task 0
"""


def read_file(filename=""):
    """
    function documented task 0
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
