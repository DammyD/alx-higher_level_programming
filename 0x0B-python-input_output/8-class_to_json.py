#!/usr/bin/python3
"""function"""


def class_to_json(obj):
    """
    function that returns the dictionary description /
    with simple data structure (list, dictionary, string, /
    integer and boolean) fir JSON serialization of an object
    Args:
        - obj: instance of class
    """

    return (obj.__dict__)
