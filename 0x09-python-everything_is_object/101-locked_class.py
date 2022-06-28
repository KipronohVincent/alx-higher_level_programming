#!/usr/bin/python3
""" Defining a class """


class LockedClass:
    """
    This class prevents user from dynamic attributes
    """
    __slots__ = ['first_name']
