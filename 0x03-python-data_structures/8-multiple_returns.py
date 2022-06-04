#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None, None
    if len(sentence) == 0:
        return None, None
    return sentence[0], sentence[-1]
