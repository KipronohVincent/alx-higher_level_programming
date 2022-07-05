#!/usr/bin/python3
""" Writing a string that returns the number of characters written """


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        return f.write(text)
