#!/usr/bin/python3
"""function"""


import json


def load_from_json_file(filename):
    """function that creates an object from a JSON file
    Args:
        - filename: path
    """

    with open(filename, 'r', encoding="UTF-8") as _file:
        return (json.loads(_file.read()))
