#!/usr/bin/python3
"""
validate if a class inherits from a_class
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited
    (directly or indirectly) from the specific class; otherwise False.
    """
    if type(obj) == a_class:
        return (False)
    return isinstance(obj, a_class)
