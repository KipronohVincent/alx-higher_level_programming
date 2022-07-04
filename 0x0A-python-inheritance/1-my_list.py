#!/usr/bin/python3
""" Creating Mylist class """


class MyList(list):
    """
    MyList class that inherits from list
    """
    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the list in sorted order
        """
        print(sorted(self))
