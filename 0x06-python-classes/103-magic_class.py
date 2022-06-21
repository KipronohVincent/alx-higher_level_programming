#!/usr/bin/python3
""" Creating a magicClass  """

import math


class MagicClass:
    """ Defining a class magicClass """
    def __init__(self, radious=0):
        """ Initializing a magicClass class
        Args: radious=0: radious of the magicClass
         """
        self.__radious = 0
        if type(radious) is not int and type(radious) is not float:
            raise TypeError("radious must be a number")

        self.__radious = radious

        def area(self):
            """ Calculating the area of the magicClass """
            return (self.__radious ** 2) * math.pi

        def circumference(self):
            """ Calculating the circumference of the magicClass """
            return 2 * math.pi * self.__radious
