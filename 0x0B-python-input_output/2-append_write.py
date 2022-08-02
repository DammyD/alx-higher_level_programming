#!/usr/bin/python3
"""
A script that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Returns the number of character
    """
    count = 0
    with open(filename, 'a', encoding="UTF-8") as f:
        for c in text:
            f.write(c)
            count += 1

            return (count)
