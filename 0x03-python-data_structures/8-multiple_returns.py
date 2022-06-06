#!/usr/bin/python3
"""
If sentence is empty, the first character should be equal to None.
"""


def multiple_returns(sentence):
    if sentence == "":
        return None, None
    else:
        return sentence[0], sentence[-1]
