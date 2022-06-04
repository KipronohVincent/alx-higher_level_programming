#!/usr/bin/python3
"""
A function that returns a tuple with the length of a string and its first character.
"""
def multiple_returns(sentence):
    if sentence is None:
        return None, None
    if len(sentence) == 0:
        return 0, ""
    return len(sentence), sentence[0]
