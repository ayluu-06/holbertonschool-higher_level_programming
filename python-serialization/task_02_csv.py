#!/usr/bin/python3

"""
module documented task 02
"""


import csv
import json


def convert_csv_to_json(filename):
    """
    function documented task 02
    """
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
        with open("data.json", "w") as file:
            json.dump(data, file)

        return True
    except Exception:
        return False
