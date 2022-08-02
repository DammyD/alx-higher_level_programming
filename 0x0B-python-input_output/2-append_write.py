#!/usr/bin/python3
"""
A script that appends a string
"""


def append_write(filename="", text=""):
    """
    Function returns the...
    """
    count = 0
    with open(filename, 'a', encoding="UTF-8") as f:
        for c in text:
            f.write(c)
            count += 1

            return (count)
