#!/usr/bin/python3

"""
module documented task 5
"""


import json


def save_to_json_file(my_obj, filename):
    """
    function documented task 5
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
