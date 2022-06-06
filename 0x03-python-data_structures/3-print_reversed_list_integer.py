#!/usr/bin/python3
"""
A function that prints all integers of a list, in reverse order.
"""


def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)-1, -1, -1):
        print(f"{my_list[i]}")
