#!/usr/bin/python3
"""
This script reads a text file in UTF-8 format and prints it to standard output
"""


def read_file(filename=""):
    """ Function that reads a file to screen"""
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            print(line, end='')
