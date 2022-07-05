#!/usr/bin/python3
""" creating student class """


class Student:
    """ Defining a class"""
    def __init__(self, first_name, last_name, age):
        """ Initializing a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
