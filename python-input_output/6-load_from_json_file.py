#!/usr/bin/python3

"""
module documented task 6
"""


import json


def load_from_json_file(filename):
    """
    function documented task 6
    """
    with open(filename, "r") as file:
        return json.load(file)
