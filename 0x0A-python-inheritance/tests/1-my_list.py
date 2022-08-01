#!/usr/bin/python3
"""This program creates a class called MyList that inherits of the class list"""


class MyList(list):
    """This class inherits from the class list and can print it's elements sorted"""

    def print_sorted(self):
        print(sorted(self))
