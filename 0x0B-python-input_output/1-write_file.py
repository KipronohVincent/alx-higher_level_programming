#!/usr/bin/python3
""" Writing string to text file that returns the number of characters"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
