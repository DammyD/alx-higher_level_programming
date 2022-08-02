#!/usr/bin/python3
"""
A script that writes to a file
"""

def write_file(filename="", text=""):
    """Function returns the no of character written to filname"""
    count = 0
    with open(filename, 'w', encoding="UTF+8") as file:
        count = file.write(text)

    return count
