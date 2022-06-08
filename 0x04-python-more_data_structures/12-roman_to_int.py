#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert a roman numeral to an integer
    You can assume the number will be between 1 to 3999.
    If the roman_string is not a string or None, return 0
    """
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            num += roman_dict[roman_string[i]]
        elif roman_dict[roman_string[i]] >= roman_dict[roman_string[i+1]]:
            num += roman_dict[roman_string[i]]
        else:
            num -= roman_dict[roman_string[i]]
    return num
