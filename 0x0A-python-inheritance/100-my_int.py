#!/usr/bin/python3
""" Creating a class """


class MyInt:
    """MyInt is a rebel. MyInt has == and != operators inverted"""
    def __init__(self, value):
        """ __init__ method """
        self.value = value

    def __eq__(self, value):
        """ __eq__ method """
        return self.value != value

    def __ne__(self, value):
        """ __ne__ method """
        return self.value == value
