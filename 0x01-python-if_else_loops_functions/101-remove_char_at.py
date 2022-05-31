#!/usr/bin/python3


def remove_char_at(str, n):
    str_copy = str
    if (str):
        str = str[:n] + str[n + 1:]
    if (n < 0):
        str = str_copy
    return (str)
