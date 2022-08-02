#!/usr/bin/python3
"""
A JSON script
"""


import json


def to_json_string(my_obj):
    """
    representation of an object
    """
    new = json.dumps(my_obj)
    return (new)
