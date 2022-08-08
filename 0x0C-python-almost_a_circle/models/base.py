#!/usr/bin/python3
"""This program is a class forother classes"""


class Base:
    """public class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of base Class with id
        Args:
            - id: int
         """
         if (id is not None):
             self.id = id
         else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects
