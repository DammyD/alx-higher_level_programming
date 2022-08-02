#!/usr/bin/python3
"""
A script that appends a string
"""


def append_write(filename="", text=""):
    """
    Function returns the no of char added
    """
    count = 0
    with open(filename, 'a', encoding="UTF-8") as file:
        count = file.write(text)

            return count
