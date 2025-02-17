#!/usr/bin/python3

"""
module documented task 00
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    function decumented task 00
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, 'r') as f:
        return json.load(f)
