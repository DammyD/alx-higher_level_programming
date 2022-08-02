#!/usr/bin/python3
"""function"""


import json


def from_json_string(my_str):
    """
    function that returns the JSON representation of an object (string)
    Args:
        - my_str: str
    """
    return (json.loads(my_str))
