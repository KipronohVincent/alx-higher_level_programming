#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if(my_list is not None):
        my_list.reverse()
        for list in my_list:
            print(f"{list:d}")
