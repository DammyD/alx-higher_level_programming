#!/usr/bin/python3
"""function"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text file, using a /
    JSON representation.
    Args:
        - my_obj
        - filename: str
    """

    with open(filename, 'w', encoding="UTF-8") as _file:
        _file.write(json.dumps(my_obj))
