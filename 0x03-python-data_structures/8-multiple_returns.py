#!/usr/bin/python3
"""
If sentence is empty, the first character should be equal to None.
"""


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        return len((sentence), sentence[0])
