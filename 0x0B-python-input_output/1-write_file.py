#!/usr/bin/python3
"""function"""


def write_file(filename="", text=""):
    """
    function  that writes a string to a text file (UTF8) and returns the /
    number of character written to filname
    """
    count = 0
    with open(filename, 'w', encoding="UTF-8") as file:
        count = file.write(text)

    return count
